# Copyright 2019 (C) github.com/Lord-of-Algorithms
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from enum import Enum


class NumberDigit(Enum):
    TWO_DIGIT = 2
    THREE_DIGIT = 3
    FOUR_DIGIT = 4
    digit = 0

    def __init__(self, digit):
        self.digit = digit


class BinaryTreePrinter:
    _MAX_LEVEL = 6
    _BLANK = " "

    _min_node_key_value = 0
    _max_node_key_value = 0
    _key_node_value_digits = 0

    #   Prints the binary tree
    @staticmethod
    def print_tree(root):
        BinaryTreePrinter._print(root, NumberDigit.TWO_DIGIT, BinaryTreePrinter._MAX_LEVEL)

    #   Prints the binary tree
    @staticmethod
    def _print(root, key_number_digit, max_tree_level):
        if root is None:
            print("The tree is empty.")
            return
        BinaryTreePrinter._key_node_value_digits = key_number_digit.digit
        BinaryTreePrinter._calculate_valid_max_node_key_value(key_number_digit)
        max_level = BinaryTreePrinter._get_tree_max_level(root)
        if max_level > max_tree_level:
            raise Exception(
                "\n\n\n" + "==========================================" +
                "\nMax level of the binary tree that can be printed is " +
                str(max_tree_level) + ". Current level is " + str(max_level) +
                ".\n==========================================\n\n\n")
        if max_level == max_tree_level:
            #  We reduce the length of edges connecting the nodes. It doesn't change the
            #  structure of the tree,
            #  but makes the printed tree smaller. We do it only for edge case, when level
            #  of tree equals to maxTreeLevel.
            max_level -= 1
        level_map = dict()
        #  position plays a role
        level = 0
        BinaryTreePrinter._fill_level_map(root, level, level_map)
        node_start_margin_map = dict()
        BinaryTreePrinter._fill_node_start_margin_map(root, level_map, True, 0,
                                                      False, node_start_margin_map,
                                                      max_level - 1)
        print("\n")
        BinaryTreePrinter._print_binary_tree(root, max_level - 1,
                                             node_start_margin_map, level_map)
        print("\n")

    @staticmethod
    def _calculate_valid_max_node_key_value(key_number_digit):
        if key_number_digit == NumberDigit.THREE_DIGIT:
            BinaryTreePrinter._max_node_key_value = 999
        elif key_number_digit == NumberDigit.FOUR_DIGIT:
            BinaryTreePrinter._max_node_key_value = 9999
        else:
            BinaryTreePrinter._max_node_key_value = 99

    @staticmethod
    def _get_tree_max_level(node):
        if node is None:
            return 0
        return max(BinaryTreePrinter._get_tree_max_level(node.get_left()),
                   BinaryTreePrinter._get_tree_max_level(node.get_right())) + 1

    # Associates each node with its level in the binary tree.
    @staticmethod
    def _fill_level_map(root, level, level_map):
        if root is not None:
            if (root.get_key() < BinaryTreePrinter._min_node_key_value
                    or root.get_key() > BinaryTreePrinter._max_node_key_value):
                raise Exception(
                    "\n\n\n" + "==========================================" +
                    "\nThe key of the node must be >= " +
                    str(BinaryTreePrinter._min_node_key_value) + " and <= " +
                    str(BinaryTreePrinter._max_node_key_value) +
                    "\n==========================================\n\n\n")
            BinaryTreePrinter._fill_level_map(root.get_left(), level + 1, level_map)
            level_map[root] = level
            BinaryTreePrinter._fill_level_map(root.get_right(), level + 1, level_map)

    #   Calculates startMargin for each node (in pre-order way) and associate this
    #   value with this node by using a map. Later these margins will be used for
    #   printing.
    #
    #   startMargin start - means from the left (to not mix with left child.
    #   There is no connection between these terms).
    @staticmethod
    def _fill_node_start_margin_map(root, node_level_map, is_root, start_margin,
                                    is_left_child, node_start_margin_map, max_level):
        if root is not None:
            node_level = node_level_map.get(root)
            #  Each level has its own space between nodes
            space_between_nodes = BinaryTreePrinter._key_node_value_digits * (
                    int(pow(2, (max_level - node_level + 1))) - 1)
            if is_root:
                start_margin = BinaryTreePrinter._key_node_value_digits * (
                        int(pow(2, (max_level - node_level))) - 1)
            elif is_left_child:
                #  for left child the margin is smaller
                start_margin = start_margin - int(
                    space_between_nodes /
                    BinaryTreePrinter._key_node_value_digits) - int(
                    BinaryTreePrinter._key_node_value_digits / 2)
            else:
                #  for right child the margin is bigger
                start_margin = start_margin + int(
                    space_between_nodes /
                    BinaryTreePrinter._key_node_value_digits) + int(
                    BinaryTreePrinter._key_node_value_digits / 2)
            node_start_margin_map[root] = start_margin
            BinaryTreePrinter._fill_node_start_margin_map(root.get_left(), node_level_map,
                                                          False, start_margin, True,
                                                          node_start_margin_map,
                                                          max_level)
            BinaryTreePrinter._fill_node_start_margin_map(root.get_right(), node_level_map,
                                                          False, start_margin, False,
                                                          node_start_margin_map,
                                                          max_level)

    #   Uses breadth-first traversal to print the nodes
    @staticmethod
    def _print_binary_tree(root, max_level, start_margin_map, level_map):
        if root is not None:
            queue = [root]
            current_level = 0
            current_position = 0
            while len(queue) > 0:
                node = queue.pop(0)
                #  Get the level and margin from the maps for given node.
                start_margin = start_margin_map.get(node)
                level = level_map.get(node)
                if current_level != level:
                    #  New level - go to next line
                    print()
                    edge_height = pow(2, max_level - current_level) - 1
                    i = 0
                    while i < edge_height:
                        BinaryTreePrinter._print_edges(current_level,
                                                       start_margin_map, level_map,
                                                       i)
                        i += 1
                    current_level = level
                    current_position = 0
                #  Because each node in the level is printed not from 0 position
                #  we need to subtract node's start_margin with current position.
                spaces_between_nodes = start_margin - current_position
                i = 0
                while i < spaces_between_nodes:
                    print(BinaryTreePrinter._BLANK, end="")
                    current_position += 1
                    i += 1
                BinaryTreePrinter._print_node(node)
                #  Remember that each number occupies keyNodeValueDigits digits. So
                #  we need to increase the current position on this value.
                current_position += BinaryTreePrinter._key_node_value_digits
                if node.get_left() is not None:
                    queue.append(node.get_left())
                if node.get_right() is not None:
                    queue.append(node.get_right())

    #   Prints the value of the node's key.
    #   Here we adjust the "x-position" of the value to get the good-looking view.
    @staticmethod
    def _print_node(node):
        key = node.get_key()
        if (BinaryTreePrinter._key_node_value_digits ==
                NumberDigit.TWO_DIGIT.digit):
            if key < 10:
                print(f"{BinaryTreePrinter._BLANK}{node}", end="")
            else:
                print(node, end="")
        elif (BinaryTreePrinter._key_node_value_digits ==
              NumberDigit.THREE_DIGIT.digit):
            if key < 10:
                print(f"{BinaryTreePrinter._BLANK}{node}{BinaryTreePrinter._BLANK}",
                      end="")
            elif key < 100:
                print(f"{node}{BinaryTreePrinter._BLANK}", end="")
            else:
                print(node, end="")
        elif (BinaryTreePrinter._key_node_value_digits ==
              NumberDigit.FOUR_DIGIT.digit):
            if key < 10:
                print(f"{BinaryTreePrinter._BLANK}{node}{BinaryTreePrinter._BLANK}{BinaryTreePrinter._BLANK}",
                      end="")
            elif key < 100:
                print(f"{BinaryTreePrinter._BLANK}{node}{BinaryTreePrinter._BLANK}",
                      end="")
            elif key < 1000:
                print(f"{node}{BinaryTreePrinter._BLANK}", end="")
            else:
                print(node, end="")

    @staticmethod
    def _print_edges(current_level, start_margin_map, level_map, iteration):
        #  Get the list of nodes for each currentLevel
        level_node_keys = []
        for k, v in level_map.items():
            node_key = k
            level = v
            if level == current_level:
                level_node_keys.append(node_key)
        space_between_slash_and_back_slash = ""
        #  The space between slash and backslash increases on two positions each iteration
        space_between_slash_and_back_slash = space_between_slash_and_back_slash.join(
            ["\0"] * (max(0, 2 * iteration))).replace("\0", BinaryTreePrinter._BLANK)
        current_position = 0
        for node in level_node_keys:
            start_margin = start_margin_map.get(node)
            slash_position = start_margin - current_position - iteration + (
                    int(BinaryTreePrinter._key_node_value_digits / 2) - 1)
            #  Starting from the left border we print the blanks
            i = 0
            while i < slash_position:
                print(BinaryTreePrinter._BLANK, end="")
                current_position += 1
                i += 1
            #  If the node doesn't have a child, we replace the child's place with a blank.
            slash = "/" if node.get_left() is not None else BinaryTreePrinter._BLANK
            back_slash = "\\" if node.get_right() is not None else BinaryTreePrinter._BLANK
            print(slash + str(space_between_slash_and_back_slash) + back_slash,
                  end="")
            current_position += 2 * (iteration + 1)
        print("")
