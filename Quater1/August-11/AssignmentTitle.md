# Assignment Title: Exploring Python List Methods


## Objective

In this assignment, you will explore and document various methods associated with the Python list data structure. You will provide explanations for each method, include examples of their usage, and specify the return type of each method.



- **Description:** A brief explanation of what the method does.
- **Syntax:** How the method is used, including its parameters.
- **Return Type:** Specify what type of value the method returns (e.g., None, a new list, a boolean, etc.).

### Methods Start:

1. **`append()` Method**
   - **Description:** Adds a single item to the end of the list.
   - **Syntax:** `list.append(item)`
     - `item`: The item to be added to the end of the list.
   - **Return Type:** `None` (modifies the list in place).
   - **Example:**
     ```python
     fruits = ['apple', 'banana']
     fruits.append('orange')
     print(fruits)  # Output: ['apple', 'banana', 'orange']
     ```

2. **`extend()` Method**
   - **Description:** Adds elements from an iterable to the end of the list.
   - **Syntax:** `list.extend(iterable)`
     - `iterable`: An iterable like another list whose elements are added.
   - **Return Type:** `None` (modifies the list in place).
   - **Example:**
     ```python
     fruits = ['apple', 'banana']
     more_fruits = ['orange', 'pineapple']
     fruits.extend(more_fruits)
     print(fruits)  # Output: ['apple', 'banana', 'orange', 'pineapple']
     ```

3. **`insert()` Method**
   - **Description:** Inserts an item at a given position.
   - **Syntax:** `list.insert(index, item)`
     - `index`: The position where the item should be inserted.
     - `item`: The item to be inserted.
   - **Return Type:** `None` (modifies the list in place).
   - **Example:**
     ```python
     fruits = ['apple', 'banana']
     fruits.insert(1, 'orange')
     print(fruits)  # Output: ['apple', 'orange', 'banana']
     ```

4. **`remove()` Method**
   - **Description:** Removes the first occurrence of the specified item from the list.
   - **Syntax:** `list.remove(item)`
     - `item`: The item to be removed.
   - **Return Type:** `None` (modifies the list in place).
   - **Example:**
     ```python
     fruits = ['apple', 'banana', 'orange']
     fruits.remove('banana')
     print(fruits)  # Output: ['apple', 'orange']
     ```

5. **`pop()` Method**
   - **Description:** Removes and returns the item at the given position. If no index is specified, removes and returns the last item.
   - **Syntax:** `list.pop([index])`
     - `index`: (Optional) The position of the item to be removed and returned.
   - **Return Type:** The removed item.
   - **Example:**
     ```python
     fruits = ['apple', 'banana', 'orange']
     fruit = fruits.pop()
     print(fruit)  # Output: 'orange'
     print(fruits)  # Output: ['apple', 'banana']
     ```

6. **`clear()` Method**
   - **Description:** Removes all items from the list, leaving it empty.
   - **Syntax:** `list.clear()`
   - **Return Type:** `None` (modifies the list in place).
   - **Example:**
     ```python
     fruits = ['apple', 'banana', 'orange']
     fruits.clear()
     print(fruits)  # Output: []
     ```

7. **`index()` Method**
   - **Description:** Returns the index of the first occurrence of the specified item.
   - **Syntax:** `list.index(item)`
     - `item`: The item whose index is to be found.
   - **Return Type:** `int` (the index of the item).
   - **Example:**
     ```python
     fruits = ['apple', 'banana', 'orange']
     index = fruits.index('banana')
     print(index)  # Output: 1
     ```

8. **`count()` Method**
   - **Description:** Returns the number of occurrences of the specified item in the list.
   - **Syntax:** `list.count(item)`
     - `item`: The item to count in the list.
   - **Return Type:** `int` (the count of the item).
   - **Example:**
     ```python
     fruits = ['apple', 'banana', 'orange', 'banana']
     count = fruits.count('banana')
     print(count)  # Output: 2
     ```

9. **`sort()` Method**
   - **Description:** Sorts the items of the list in ascending order by default.
   - **Syntax:** `list.sort(key=None, reverse=False)`
     - `key`: (Optional) A function to customize the sorting.
     - `reverse`: (Optional) If `True`, sorts in descending order.
   - **Return Type:** `None` (modifies the list in place).
   - **Example:**
     ```python
     fruits = ['banana', 'apple', 'orange']
     fruits.sort()
     print(fruits)  # Output: ['apple', 'banana', 'orange']
     ```

10. **`reverse()` Method**
    - **Description:** Reverses the order of the items in the list.
    - **Syntax:** `list.reverse()`
    - **Return Type:** `None` (modifies the list in place).
    - **Example:**
      ```python
      fruits = ['apple', 'banana', 'orange']
      fruits.reverse()
      print(fruits)  # Output: ['orange', 'banana', 'apple']
      ```

11. **`copy()` Method**
    - **Description:** Returns a shallow copy of the list.
    - **Syntax:** `list.copy()`
    - **Return Type:** `list` (a new list that is a shallow copy of the original).
    - **Example:**
      ```python
      fruits = ['apple', 'banana', 'orange']
      fruits_copy = fruits.copy()
      print(fruits_copy)  # Output: ['apple', 'banana', 'orange']
      ```
-------------------

# Python List Methods

## 1. `append()` Method
**Kaam:** Yeh method list ke end mein ek naya item add karne ke liye hota hai. Jaise agar aapki shopping list mein already kuch cheezein hain, aur aap ek aur cheez uske end mein daalna chahte hain, toh `append()` ussi ke liye hota hai.

## 2. `extend()` Method
**Kaam:** Agar aap apni list mein aur cheezein ek aur list se jodna chahte hain, toh `extend()` use hota hai. Yeh doosri list ke sab items ko aapki pehli list mein daal deta hai.

## 3. `insert()` Method
**Kaam:** Agar aap kisi specific jagah par apni list mein kuch daalna chahte hain, toh `insert()` kaam aata hai. Yeh kisi bhi position par item ko add karne ke liye hota hai, sirf end mein nahi.

## 4. `remove()` Method
**Kaam:** Yeh method list se kisi specific item ko nikaalne ke liye hota hai. Lekin yeh sirf us item ka pehla occurrence hi nikaalta hai, agar voh list mein multiple times ho.

## 5. `pop()` Method
**Kaam:** `pop()` method list se ek item nikaal kar aapko wapas de deta hai. Agar aap nahi batate ke kis position se nikaalna hai, toh yeh last item ko nikaal leta hai.

## 6. `clear()` Method
**Kaam:** Yeh method puri list ko khali karne ke liye hota hai. Isse saari cheezein list se nikal jaati hain.

## 7. `index()` Method
**Kaam:** Agar aapko pata karna hai ke aapki list mein koi item kahan pe hai, toh `index()` us item ka position bata deta hai.

## 8. `count()` Method
**Kaam:** Yeh method batata hai ke aapki list mein koi item kitni baar aaya hai.

## 9. `sort()` Method
**Kaam:** `sort()` list ke items ko arrange karne ke liye hota hai. Yeh default mein chhote se bade ya A se Z tak sort karta hai.

## 10. `reverse()` Method
**Kaam:** Yeh method list ke items ko ulta kar deta hai, yani list ko reverse order mein kar deta hai.

## 11. `copy()` Method
**Kaam:** Agar aap apni list ki ek nayi copy banana chahte hain, toh `copy()` usi ke liye hota hai. Yeh ek nayi list banata hai jo original list jaisi hoti hai.

ya sab good but is ma add karo 
Description: A brief explanation of what the method does.
Syntax: How the method is used, including its parameters.
Return Type: Specify what type of value the method returns (e.g., None, a new list, a boolean, etc.).