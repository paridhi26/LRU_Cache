# LRU Cache

A simple and efficient implementation of a **Least Recently Used (LRU) Cache** using a **hash map** and a **doubly linked list** in Python. Designed for constant-time `get` and `put` operations.

---

## 📌 Features

- O(1) time complexity for both `get` and `put`
- Custom implementation of a **doubly linked list**
- Automatically evicts the **Least Recently Used** item when capacity is exceeded
- Easy-to-read internal structure for debugging and visualization

---

## 📦 Data Structures Used

- **Hash Map (`dict`)**: For fast key lookup.
- **Doubly Linked List**: Maintains access order.
  - Head: Most Recently Used (MRU)
  - Tail: Least Recently Used (LRU)

---

## 🚀 Usage Example

```python
cache = LRUCache(2)

cache.put(1, 1)       # Cache is {1=1}
print(cache)

cache.put(2, 2)       # Cache is {2=2, 1=1}
print(cache)

cache.get(1)          # Returns 1, Cache becomes {1=1, 2=2}
print(cache)

cache.put(3, 3)       # Evicts key 2, Cache becomes {3=3, 1=1}
print(cache)

cache.get(2)          # Returns -1 (not found)
```

---

## 📘 Class API

### `LRUCache(capacity: int)`

Initialize the cache with a given capacity.

---

### `put(key: int, value: int) -> None`

Add a key-value pair to the cache.  
If the key exists, update the value and mark it as recently used.  
If capacity is exceeded, the least recently used item is evicted.

---

### `get(key: int) -> int`

Return the value for the given key if it exists, and mark it as recently used.  
Returns `-1` if the key is not present.

---

### `__str__()`

Returns a string representation of the cache contents from **MRU to LRU**.

---

## 🛠️ Internal Helpers

- `_add_to_front(node)` – Inserts node right after `head`
- `_remove(node)` – Detaches node from the list
- `_move_to_front(node)` – Moves an existing node to the front
- `_evict_from_back()` – Removes and returns the LRU node

---

## ✅ Requirements

- Python 3.6+

---

## 📄 License

This project is open-source and free to use under the MIT License.
