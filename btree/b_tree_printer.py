"""Draws a BTree on the console.

The drawing puts every node of a level on one line and joins each node to
its children with a bar, so that the shape of the tree — how wide the nodes
are and how they divide the keys between them — can be read at a glance::

                         [50]
                           |
                +---------------------+
             [20 35]                [65]
                |                     |
       +--------+--------+        +-------+
    [10 15]  [25 30]  [40 45]  [55 60]  [70]

A wide tree does not fit a console, so ``print_tree`` falls back to
``outline``, which spends one line per node and marks the levels by
indentation instead::

    [50]
        [20 35]
            [10 15]
            [25 30]
            [40 45]
        [65]
            [55 60]
            [70]

An empty tree is a single node holding no keys, and both views show it
as ``[]``.
"""


class _Block:
    """A subtree as it will be drawn: the lines it occupies, the width they
    share, and the column its own root is centred on."""

    def __init__(self, lines, width, center):
        self.lines = lines
        self.width = width
        self.center = center

    def line(self, row):
        """Return the given line, padded to the block's width so that
        whatever is drawn to the right of it starts at the same column on
        every line."""
        line = self.lines[row] if row < len(self.lines) else ''
        return line.ljust(self.width)


class BTreePrinter:
    """Draws a BTree. The printer belongs to the same package as the tree
    and reads its nodes directly."""

    # Columns between two neighbouring subtrees.
    _GAP = 2

    # The widest drawing print_tree will show. Beyond it the lines wrap
    # around the console and the picture is worth less than the outline.
    _MAX_WIDTH = 110

    @staticmethod
    def print_tree(tree):
        """Print the tree — drawn if the drawing fits the console, as an
        outline if it does not — and a blank line after it."""
        drawing = BTreePrinter.draw(tree)
        width = max(len(line) for line in drawing.splitlines())
        if width > BTreePrinter._MAX_WIDTH:
            print('(too wide to draw — the outline instead)')
            print(BTreePrinter.outline(tree), end='')
        else:
            print(drawing, end='')
        print()

    @staticmethod
    def draw(tree):
        """Return the tree drawn level by level, each node joined to its
        children by a bar. The drawing is as wide as it needs to be."""
        block = BTreePrinter._layout(tree._root)
        return ''.join(line.rstrip() + '\n' for line in block.lines)

    @staticmethod
    def outline(tree):
        """Return the tree with one node per line, each child indented under
        its parent. Unlike ``draw``, this stays narrow however large the tree
        grows."""
        lines = []
        BTreePrinter._append_outline(lines, tree._root, 0)
        return ''.join(lines)

    @staticmethod
    def _append_outline(lines, node, depth):
        lines.append('    ' * depth + BTreePrinter._label(node) + '\n')
        for child in node.children:
            BTreePrinter._append_outline(lines, child, depth + 1)

    @staticmethod
    def _label(node):
        # A node the way it is drawn: its keys in ascending order, in
        # brackets.
        return '[' + ' '.join(str(key) for key in node.keys) + ']'

    @staticmethod
    def _layout(node):
        """Lay out the subtree rooted at the node: the children first, side
        by side, and then the node itself above the middle of them."""
        label = BTreePrinter._label(node)
        if node.is_leaf():
            return _Block([label], len(label), len(label) // 2)

        # The children stand in a row, a gap apart. Each one is drawn from
        # the column its own block starts at, so its root ends up at that
        # column plus the block's centre.
        children = []
        centers = []
        children_width = 0
        for child in node.children:
            block = BTreePrinter._layout(child)
            if children_width > 0:
                children_width += BTreePrinter._GAP
            children.append(block)
            centers.append(children_width + block.center)
            children_width += block.width

        # The label sits above the middle child, or halfway between the two
        # middle ones when the count is even — that keeps it over the middle
        # of the row however wide the children turn out to be. A label wider
        # than that middle would hang off the left edge, so everything below
        # it moves right instead.
        middle = len(centers) // 2
        center = (centers[middle] if len(centers) % 2 == 1
                  else (centers[middle - 1] + centers[middle]) // 2)
        shift = max(0, len(label) // 2 - center)
        center += shift
        label_start = center - len(label) // 2
        width = max(shift + children_width, label_start + len(label))

        lines = [' ' * label_start + label,
                 ' ' * center + '|',
                 BTreePrinter._bar(centers, shift, width)]
        lines.extend(BTreePrinter._side_by_side(children, shift))
        return _Block(lines, width, center)

    @staticmethod
    def _bar(centers, shift, width):
        """Build the line that joins a node to its children: a bar reaching
        from the first child to the last, with a + where each child hangs
        from it. The node above meets the bar where its own line comes
        down."""
        line = [' '] * width
        for i in range(centers[0] + shift, centers[-1] + shift + 1):
            line[i] = '-'
        for child_center in centers:
            line[child_center + shift] = '+'
        return ''.join(line)

    @staticmethod
    def _side_by_side(children, shift):
        """Put the children's blocks next to each other, a gap apart,
        shifted as far right as the node above them needs. The blocks may
        differ in height only when the tree is broken, and a short one is
        then filled out with blank lines."""
        height = max(len(child.lines) for child in children)
        lines = []
        for row in range(height):
            gap = ' ' * BTreePrinter._GAP
            lines.append(' ' * shift
                         + gap.join(child.line(row) for child in children))
        return lines
