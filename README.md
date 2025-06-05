# Order Statistics

This project implements fundamental Order Statistics algorithms, focusing on techniques to efficiently find specific elements within a dataset. It includes algorithms to determine the maximum and minimum values in a list, as well as methods to select the i-th smallest element, such as the Randomized Select and Deterministic Select algorithms. These implementations highlight key strategies in algorithm design, including divide-and-conquer and probabilistic approaches, and are useful for problems in data analysis, optimization, and real-time systems where quick selection or extreme value identification is critical.

## Objectives

- Implement algorithms to find the maximum and minimum values in a list.
- Implement the Randomized Select and Deterministic Select algorithms to find the i-th smallest element in a list, and compare their performance with sorting the whole list and selecting the i-th element.
- Understand the time complexity and efficiency of these algorithms.

## Conclusion

This project provided a comprehensive study of order statistics, covering both the problems of finding minimum/maximum values and selecting the i-th smallest element in a list. We demonstrated that algorithmic optimizations—such as reducing unnecessary comparisons or using efficient selection algorithms—can lead to substantial performance improvements. In particular, for selecting a single order statistic, algorithms like `random_select` and `deterministic_select` are far more efficient than sorting the entire list. These findings highlight the importance of choosing the right algorithm for the task, especially when working with large datasets.

## **Project Structure**

The repository is organized into the following components:

- **`1 Minimum and Maximum` Folder**:  
  This folder contains the implementation of `min_value`, `max_value`, `min_and_max` and `min_and_max_optimized` algorithms, which find the minimum and maximum values in a list. It includes an experiment measuring and analyzing their execution times.

- **`2 Selection Algorithms` Folder**:  
  This folder contains the implementation of the `random_select`, `deterministic_select` and `quicksort_select` algorithms, which are used to find the i-th smallest element in a list. It includes an experiment measuring and analyzing their execution times against sorting the entire list.

- **`img` Folder**:  
  Stores the output images generated during experimentation.  

- **`project_functions.py` Python Script**:  
  This Python script includes all the algorithms developed specifically for this project.

- `requirements.txt` Text File:   
  This file lists all the dependencies required to run the project.

## **Final Note**

The system developed for this project was created solely for academic purposes. It is not designed to be an optimal or production-grade benchmarking tool.

## **Reference**

This project follows the structure and theoretical foundations presented in the following textbook:

> Cormen, Thomas H., Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.  
> *Introduction to Algorithms*. Fourth Edition.  
> Cambridge, Massachusetts; London, England: The MIT Press, 2022.  
> ISBN: 9780262046305  
> LCCN: 2021037260  
> Available at: [https://lccn.loc.gov/2021037260](https://lccn.loc.gov/2021037260)

> Byron Velasco, 2025.  
> *Sorting Algorithms* (GitHub Repository).  
> Available at: [https://github.com/ByronVelasco/SortingAlgorithms](https://github.com/ByronVelasco/SortingAlgorithms)

## **License**

- The **source code** of this project is licensed under the [MIT License](./LICENSE).  
  You are free to use, modify, and distribute the code with proper attribution.

- The **educational content** (including explanations, diagrams, and documentation) is shared under the  
  [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).  
  You may reuse and adapt it for non-commercial purposes with attribution.

---

© 2025 Byron Velasco