# WordHive-DigitalLibrary: Precision Text Management with Advanced Hashing

## Introduction
**WordHive-DigitalLibrary** is an advanced digital library management system that provides a sophisticated framework for indexing, searching, and dynamically managing textual data. Tailored for high-performance keyword searching and efficient word storage, this project is particularly suited for extensive digital libraries requiring efficient retrieval of unique terms and quick access to books via keyword-based queries. Through the integration of custom hashing and priority-based queue systems, WordHive optimizes both the storage and processing of digital text data.

Developed for IITD’s library digitization project, **WordHive-DigitalLibrary** leverages dynamic hash tables and collision-handling strategies to create a secure, optimized repository for digital text. The underlying data structures in WordHive are engineered to maintain high efficiency across varied workloads, ensuring balanced memory use and reduced retrieval latency.

## Project Overview
This project focuses on the following key objectives:
1. **Precision Text Management**: Efficiently manage, search, and store unique words and book data for rapid retrieval and reduced storage overhead.
2. **Advanced Hashing**: Employ dynamic resizing, collision handling, and polynomial hash functions for reliable data management.
3. **Keyword-Based Book Retrieval**: Implement keyword search functionality that quickly identifies books containing specified terms, enhancing user accessibility.

WordHive comprises two primary modules:
- **Static Hashing Module**: Implements a lexicographic sorting-based approach for indexing unique terms.
- **Dynamic Hashing Module**: Uses adaptive hash tables with load factor monitoring and rehashing, supporting multiple collision-handling strategies (chaining, linear probing, double hashing).

## System Architecture
The system uses a modular, hierarchical architecture with layered responsibilities for each component. The core components include:

### 1. **Hash Table Classes**
   - **HashSet** and **HashMap**: Base classes providing low-level insertion and lookup operations.
   - **DynamicHashSet** and **DynamicHashMap**: Extensions with load-based resizing, enhancing memory efficiency.
   - **Collision Handling**: Support for chaining, linear probing, and double hashing to handle collision cases with minimal overhead.

### 2. **Library Modules**
   - **MuskLibrary**: A lexicographic sorting-based module for static hash management.
   - **JGBLibrary**: A dynamic hash-based library using different strategies (Jobs, Gates, Bezos) for handling hash collisions with Chaining, Linear Probing, or Double Hashing.

## Hash Table Implementations
The hash table implementation in WordHive uses polynomial accumulation for hashing, optimized for rapid key retrieval. The following strategies are implemented to handle hash collisions:

1. **Chaining**: Implements linked lists at each hash index, allowing multiple entries per slot.
2. **Linear Probing**: Uses open addressing with sequential slot checking to resolve conflicts.
3. **Double Hashing**: Employs a secondary hash function to determine step sizes, minimizing clustering.

Dynamic resizing is managed via load factor monitoring, with tables resized when 50% capacity is reached to ensure balanced space and time efficiency.

