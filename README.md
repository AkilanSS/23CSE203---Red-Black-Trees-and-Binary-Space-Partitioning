
# Project Developers
- Adwit Singh - CB.SC.U4CSE24704
- Akilan - CB.SC.U4CSE24707
- Dishitha - CB.SC.U4CSE24713
- Mahima R Iyer- CB.SC.U4CSE24732

# File Structure
```
bsp_visualizer/
├── main.py                     # Entry point of the application.
├── README.md                   # Your project's README file (content below).
├── requirements.txt            # Lists project dependencies (e.g., pygame).
└── src/
    ├── init.py
    ├── game.py                 # The main Game class, handles the loop and state.
    ├── config.py               # Constants: screen settings, colors, etc.
    │
    ├── data_structures/
    │   ├── init.py
    │   ├── bsp_tree.py         # BSP Tree Node and Tree implementation.
    │   └── rb_tree.py          # Red-Black Tree Node and Tree implementation.
    │
    ├── geometry/
    │   ├── init.py            # Defines a LineSegment class with geometry helpers.
    │   └── line.py           # Geometric functions (intersection, splitting, etc.).
    │
    └── core/
        ├── init.py
        ├── renderer.py         # Handles all drawing operations and camera.
        └── ui_manager.py       # Manages and draws UI elements (buttons, text).
```


# BSP Tree & Red-Black Tree Visualizer

An interactive Pygame application for visualizing the construction of **Binary Space Partitioning (BSP) trees** from a set of lines. This project also uses a **Red-Black Tree** to efficiently manage the collection of line segment data.



## 📜 About The Project

This tool provides a visual, step-by-step understanding of how a BSP tree recursively partitions a 2D space. Users can draw lines on a canvas and then trigger an algorithm that builds a BSP tree from them. The resulting partition planes are visualized, offering insight into how this data structure is used in computer graphics, robotics, and game development for tasks like collision detection and visibility ordering.

The secondary goal is to demonstrate the use of a **Red-Black Tree**, a self-balancing binary search tree, for managing the set of drawn lines. Before being passed to the BSP builder, lines are stored in an R-B tree, keyed by a unique ID, allowing for efficient insertion, deletion, and retrieval ($O(\log n)$ time complexity).

## ✨ Features

* **Interactive Canvas**: Draw line segments directly on the screen with your mouse.
* **BSP Tree Construction**: Build the BSP tree from the drawn lines with a single key press.
* **Partition Visualization**: Clearly see the infinite planes used to partition the space at each node of the tree.
* **Data Management**: All line data is stored and managed by a robust Red-Black Tree.
* **Camera Controls**: Pan the view to inspect different parts of the canvas.

## 📂 File Structure Overview

The project is organized into a modular structure for clarity and scalability:

* `main.py`: The main entry point for the application.
* `src/game.py`: Contains the main `Game` class that runs the application loop and manages state.
* `src/data_structures/`: Contains the core logic for the `bsp_tree.py` and `rb_tree.py`.
* `src/geometry/`: Includes helper classes (`line.py`) and functions (`utils.py`) for geometric calculations.
* `src/core/`: Manages engine components like the `renderer.py` and `ui_manager.py`.

## 🚀 How To Use

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/bsp-visualizer.git](https://github.com/your-username/bsp-visualizer.git)
    cd bsp-visualizer
    ```
2.  **Install dependencies:**
    This project requires Pygame.
    ```sh
    pip install -r requirements.txt
    ```
3.  **Run the application:**
    ```sh
    python main.py
    ```

### Controls

* **Left Mouse Button (Drag & Drop)**: Draw a new line segment.
* **`B` Key**: Build (or rebuild) the BSP tree from the current lines.
* **`C` Key**: Clear the screen and reset all data structures.
* **Arrow Keys**: Pan the camera view around the canvas.

## 🧠 Technical Concepts

### Binary Space Partitioning (BSP) Tree

A BSP tree is a data structure that recursively subdivides a space into convex sets using hyperplanes. In 2D, these "hyperplanes" are simply lines.

1.  **Select a Partition Line**: From the set of lines, one is chosen to be the partitioner for the current node.
2.  **Partition**: All other lines are classified relative to this partition line:
    * Lines fully in **front** of the partitioner go to the "front" child node.
    * Lines fully **behind** the partitioner go to the "behind" child node.
    * Lines that **span** the partitioner are split into two pieces, which are sent to the front and behind children, respectively.
3.  **Recurse**: This process is repeated for the front and behind child nodes until every line has been used as a partitioner.

### Red-Black Tree

A Red-Black Tree is a self-balancing binary search tree that maintains its balance through a set of strict rules. Each node has a "color" (red or black), and these colors are used to ensure that the path from the root to any leaf is roughly the same length. This guarantees that insertion, deletion, and search operations remain very efficient ($O(\log n)$), even in the worst-case scenario. In this project, it's used to hold the master list of all line segments before they are processed by the BSP algorithm.

## 🛠️ Future Improvements

* Implement support for polygons instead of just line segments.
* Add a visual representation of both the BSP and Red-Black trees on a side panel.
* Create a "painter's algorithm" mode that uses the BSP tree's traversal order to render lines from back-to-front.
* Allow users to save and load line configurations from a file.

## License
<a href="https://github.com/AkilanSS/23CSE203---Red-Black-Trees-and-Binary-Space-Partitioning/tree/main">23CSE203---Red-Black-Trees-and-Binary-Space-Partitioning</a> © 2025 by <a href="https://github.com/AkilanSS">Akilan S S, Adwit Singh R, Dishitha, Mahima R Iyer</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 0.2em;max-height:0.2em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 0.2em;max-height:0.2em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 0.2em;max-height:0.2em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nd.svg" alt="" style="max-width: 0.2em;max-height:0.2em;margin-left: .2em;">
