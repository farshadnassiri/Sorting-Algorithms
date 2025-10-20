# Sorting Algorithms Performance Analysis

A comprehensive Python project that implements and compares the performance of three fundamental sorting algorithms: Bubble Sort, Insertion Sort, and Selection Sort. This project includes both theoretical analysis and practical performance measurements with visualizations.

## 🚀 Features

- **Three Sorting Algorithms**: Implementation of Bubble Sort, Insertion Sort, and Selection Sort
- **Performance Analysis**: Time and space complexity measurements
- **Visual Comparisons**: Interactive plots showing algorithm performance across different input sizes
- **Comprehensive Testing**: Unit tests for each algorithm implementation
- **Modular Design**: Clean, well-documented code structure

## 📁 Project Structure

```
Sorting Algorithms/
├── readme.md                 # This file
└── src/
    ├── bubble_sort.py       # Bubble Sort implementation
    ├── insertion_sort.py    # Insertion Sort implementation
    ├── selection_sort.py    # Selection Sort implementation
    ├── utils.py             # Utility functions for performance measurement
    └── run.ipynb           # Jupyter notebook for analysis and visualization
```

## 🔧 Algorithms Implemented

### 1. Bubble Sort
- **Time Complexity**: O(n²) average and worst case
- **Space Complexity**: O(1)
- **Description**: Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order

### 2. Insertion Sort
- **Time Complexity**: O(n²) average and worst case, O(n) best case
- **Space Complexity**: O(1)
- **Description**: Builds the final sorted array one item at a time, inserting each element into its correct position

### 3. Selection Sort
- **Time Complexity**: O(n²) in all cases
- **Space Complexity**: O(1)
- **Description**: Finds the minimum element from the unsorted portion and places it at the beginning

## 📊 Performance Analysis

The project includes comprehensive performance analysis with:

- **Time Complexity Measurement**: Actual execution time for different input sizes
- **Space Complexity Analysis**: Memory usage tracking
- **Visual Comparisons**: Matplotlib plots showing performance trends
- **Scalability Testing**: Performance across various input sizes (10, 100, 1000, 10000 elements)

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.6+
- Jupyter Notebook
- Required packages: `matplotlib`, `typing`

### Installation
1. Clone or download this repository
2. Navigate to the project directory
3. Install required dependencies:
   ```bash
   pip install matplotlib
   ```

## 🚀 Usage

### Running Individual Algorithms
Each sorting algorithm can be run independently:

```python
# Bubble Sort
from src.bubble_sort import bubble_sort
result = bubble_sort([3, 1, 4, 1, 5, 9, 2, 6])

# Insertion Sort
from src.insertion_sort import insertion_sort
result = insertion_sort([3, 1, 4, 1, 5, 9, 2, 6])

# Selection Sort
from src.selection_sort import selection_sort
result = selection_sort([3, 1, 4, 1, 5, 9, 2, 6])
```

### Running Performance Analysis
1. Open the Jupyter notebook:
   ```bash
   jupyter notebook src/run.ipynb
   ```
2. Run all cells to generate performance comparisons and visualizations

### Testing
Each algorithm includes built-in tests:
```bash
python src/bubble_sort.py
python src/insertion_sort.py
python src/selection_sort.py
python src/utils.py
```

## 📈 Results & Visualizations

The project generates two main visualizations:

1. **Time Complexity Plot**: Shows execution time vs input size for all algorithms
2. **Space Complexity Plot**: Displays memory usage patterns across different input sizes

These plots help visualize the theoretical complexity analysis in practice and demonstrate the performance characteristics of each algorithm.

## 🧪 Testing

Each algorithm includes comprehensive unit tests:
- Tests with small arrays
- Edge cases (empty arrays, single elements)
- Verification of correct sorting behavior

## 📚 Educational Value

This project serves as an excellent learning resource for:
- Understanding fundamental sorting algorithms
- Comparing algorithm performance in practice
- Learning about time and space complexity analysis
- Data visualization with Python and Matplotlib
- Clean code organization and documentation

## 🤝 Contributing

Feel free to contribute by:
- Adding more sorting algorithms
- Improving performance measurements
- Enhancing visualizations
- Adding more comprehensive tests
- Improving documentation

## 📄 License

This project is open source and available under the MIT License.

---

**Note**: This project is part of a Project-Based Python learning series and demonstrates practical implementation and analysis of fundamental computer science algorithms.
