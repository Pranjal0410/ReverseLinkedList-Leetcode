# Reverse Linked List Python

## Introduction

This Python script provides a class `Solution` with a method `reverseList` for reversing a linked list. The code utilizes a recursive approach to achieve this.

## Usage

1. Ensure you have Python installed on your system.
2. Download the `solution.py` file.
3. Use the provided `ListNode` class or define your own according to your needs.
4. Create an instance of the `Solution` class and call the `reverseList` method.

```python
# Example Usage

# Create an instance of the Solution class
solution = Solution()

# Define your linked list or use the provided ListNode class

# Reverse the linked list
reversed_list = solution.reverseList(head)

# Display the reversed linked list
# (Implement a display method or use print statements to see the result)
```

## Code Explanation

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            self.reverseList(head.next)    
            head.next.next= head
        head.next = None

        return newHead
```

### `class Solution`

Defines a class named `Solution`.

### `def reverseList(self, head: ListNode) -> ListNode:`

Defines a method named `reverseList` that takes a `ListNode` named `head` as input and returns a `ListNode`.

- Checks if `head` is `None` (i.e., if the linked list is empty). If it is, it returns `None`.
- Initializes `newHead` with the current `head`.
- Checks if there is a next node. If true, it recursively calls `self.reverseList(head.next)`, effectively moving to the next node.
- Recursively reverses the linked list.
- Recursive call. This is where the actual reversing happens.
- Reverses the link from the current node to its next node.
- Sets the `next` pointer of the current node to `None`, effectively breaking the link to the next node.
- Returns the new head of the reversed linked list.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
