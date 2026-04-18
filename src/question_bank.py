# question_bank.py
# Generic question bank organized by domain → topic
# Student picks any domain/topic they want — not branch-locked

QUESTION_BANK = {
    "Machine Learning": {
        "Supervised Learning": [
            {"q": "Which algorithm draws a hyperplane to separate classes?", "options": ["KNN", "SVM", "K-Means", "Apriori"], "answer": "SVM", "difficulty": "medium"},
            {"q": "What does overfitting mean?", "options": ["Model performs well on test data", "Model memorizes training data and fails on new data", "Model has too few parameters", "Model underfits the data"], "answer": "Model memorizes training data and fails on new data", "difficulty": "easy"},
            {"q": "Which metric is best for imbalanced classification?", "options": ["Accuracy", "F1 Score", "MSE", "R²"], "answer": "F1 Score", "difficulty": "medium"},
            {"q": "What is the purpose of a validation set?", "options": ["To train the model", "To tune hyperparameters", "To test final performance", "To normalize data"], "answer": "To tune hyperparameters", "difficulty": "medium"},
            {"q": "Which of these is a boosting algorithm?", "options": ["Random Forest", "XGBoost", "K-Means", "PCA"], "answer": "XGBoost", "difficulty": "hard"},
        ],
        "Neural Networks": [
            {"q": "What does ReLU activation do to negative values?", "options": ["Keeps them", "Sets them to 1", "Sets them to 0", "Squares them"], "answer": "Sets them to 0", "difficulty": "easy"},
            {"q": "What is backpropagation?", "options": ["Forward pass through network", "Algorithm to compute gradients and update weights", "A type of activation function", "A regularization technique"], "answer": "Algorithm to compute gradients and update weights", "difficulty": "easy"},
            {"q": "What problem does batch normalization solve?", "options": ["Overfitting", "Internal covariate shift", "Vanishing gradients only", "Class imbalance"], "answer": "Internal covariate shift", "difficulty": "hard"},
            {"q": "Dropout in neural networks is used for?", "options": ["Speed", "Regularization", "Activation", "Optimization"], "answer": "Regularization", "difficulty": "medium"},
            {"q": "Which optimizer uses adaptive learning rates per parameter?", "options": ["SGD", "Momentum", "Adam", "Perceptron"], "answer": "Adam", "difficulty": "medium"},
        ],
        "Model Evaluation": [
            {"q": "What does AUC-ROC measure?", "options": ["Regression error", "Classifier's ability to distinguish classes", "Clustering quality", "Feature importance"], "answer": "Classifier's ability to distinguish classes", "difficulty": "medium"},
            {"q": "What is k in k-fold cross validation?", "options": ["Number of features", "Number of data splits", "Number of classes", "Learning rate"], "answer": "Number of data splits", "difficulty": "easy"},
            {"q": "Precision = TP / (TP + ?)", "options": ["TN", "FN", "FP", "All of above"], "answer": "FP", "difficulty": "medium"},
            {"q": "Which score combines precision and recall?", "options": ["Accuracy", "AUC", "F1", "MSE"], "answer": "F1", "difficulty": "easy"},
            {"q": "What is the bias-variance tradeoff?", "options": ["Speed vs accuracy", "Underfitting vs overfitting", "Training vs test error", "Precision vs recall"], "answer": "Underfitting vs overfitting", "difficulty": "medium"},
        ],
    },

    "Web Development": {
        "HTML & CSS": [
            {"q": "Which HTML tag defines a hyperlink?", "options": ["<link>", "<a>", "<href>", "<url>"], "answer": "<a>", "difficulty": "easy"},
            {"q": "CSS property to make elements flexible side by side?", "options": ["display: block", "display: flex", "float: center", "position: relative"], "answer": "display: flex", "difficulty": "easy"},
            {"q": "What does the CSS box model consist of?", "options": ["Content, padding, border, margin", "Header, body, footer", "Width, height, color", "Block, inline, flex"], "answer": "Content, padding, border, margin", "difficulty": "medium"},
            {"q": "Which selector targets an element with id='main'?", "options": [".main", "#main", "main", "*main"], "answer": "#main", "difficulty": "easy"},
            {"q": "What is CSS specificity?", "options": ["Speed of CSS rendering", "Rule for which styles take priority", "Number of CSS files", "CSS file size"], "answer": "Rule for which styles take priority", "difficulty": "medium"},
        ],
        "JavaScript": [
            {"q": "What does === check in JS?", "options": ["Value only", "Type only", "Value and type", "Reference"], "answer": "Value and type", "difficulty": "easy"},
            {"q": "What is a Promise in JavaScript?", "options": ["A function", "An async operation placeholder", "A loop", "A class"], "answer": "An async operation placeholder", "difficulty": "medium"},
            {"q": "What does 'use strict' do?", "options": ["Enables strict type checking", "Prevents use of undeclared variables", "Makes JS faster", "Disables closures"], "answer": "Prevents use of undeclared variables", "difficulty": "medium"},
            {"q": "What is event bubbling?", "options": ["Event triggers parent elements too", "Event stops at target", "DOM reloads on event", "CSS animation trigger"], "answer": "Event triggers parent elements too", "difficulty": "hard"},
            {"q": "typeof null returns?", "options": ["null", "undefined", "object", "string"], "answer": "object", "difficulty": "hard"},
        ],
        "React": [
            {"q": "What hook manages state in React?", "options": ["useEffect", "useState", "useRef", "useMemo"], "answer": "useState", "difficulty": "easy"},
            {"q": "When does useEffect run by default?", "options": ["Only once", "After every render", "Before render", "Never automatically"], "answer": "After every render", "difficulty": "medium"},
            {"q": "What is the virtual DOM?", "options": ["A real browser DOM", "A JS object representing the UI", "A CSS framework", "A database"], "answer": "A JS object representing the UI", "difficulty": "easy"},
            {"q": "Props in React are?", "options": ["Mutable state", "Read-only inputs to components", "CSS classes", "Event handlers"], "answer": "Read-only inputs to components", "difficulty": "easy"},
            {"q": "What does React.memo do?", "options": ["Memoizes state", "Prevents re-render if props unchanged", "Caches API calls", "Clears memory"], "answer": "Prevents re-render if props unchanged", "difficulty": "hard"},
        ],
    },

    "Data Structures & Algorithms": {
        "Arrays & Strings": [
            {"q": "Time complexity of accessing an array element by index?", "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"], "answer": "O(1)", "difficulty": "easy"},
            {"q": "Which technique uses two pointers moving toward each other?", "options": ["Sliding window", "Two pointer", "Binary search", "DFS"], "answer": "Two pointer", "difficulty": "easy"},
            {"q": "Worst case time for bubble sort?", "options": ["O(n)", "O(n log n)", "O(n²)", "O(1)"], "answer": "O(n²)", "difficulty": "easy"},
            {"q": "What is a sliding window used for?", "options": ["Tree traversal", "Subarray/substring problems", "Graph search", "Sorting"], "answer": "Subarray/substring problems", "difficulty": "medium"},
            {"q": "Anagram check best approach?", "options": ["Sort both strings", "Use frequency hashmap", "Binary search", "Stack"], "answer": "Use frequency hashmap", "difficulty": "medium"},
        ],
        "Trees & Graphs": [
            {"q": "Inorder traversal of BST gives?", "options": ["Random order", "Sorted order", "Reverse order", "Level order"], "answer": "Sorted order", "difficulty": "easy"},
            {"q": "BFS uses which data structure?", "options": ["Stack", "Queue", "Heap", "Array"], "answer": "Queue", "difficulty": "easy"},
            {"q": "DFS uses which data structure?", "options": ["Queue", "Stack", "Linked list", "Set"], "answer": "Stack", "difficulty": "easy"},
            {"q": "Dijkstra's algorithm finds?", "options": ["Minimum spanning tree", "Shortest path", "Topological order", "Connected components"], "answer": "Shortest path", "difficulty": "medium"},
            {"q": "What is a balanced BST?", "options": ["All leaves at same level", "Height difference of subtrees ≤ 1", "All nodes have 2 children", "Root has no children"], "answer": "Height difference of subtrees ≤ 1", "difficulty": "medium"},
        ],
        "Dynamic Programming": [
            {"q": "DP solves problems by?", "options": ["Brute force", "Storing subproblem results", "Greedy choices", "Random sampling"], "answer": "Storing subproblem results", "difficulty": "easy"},
            {"q": "Top-down DP is also called?", "options": ["Tabulation", "Memoization", "Greedy", "Backtracking"], "answer": "Memoization", "difficulty": "easy"},
            {"q": "Which problem is classic DP?", "options": ["Binary search", "Fibonacci sequence", "BFS", "Quicksort"], "answer": "Fibonacci sequence", "difficulty": "easy"},
            {"q": "Longest Common Subsequence time complexity?", "options": ["O(n)", "O(n log n)", "O(n²)", "O(2ⁿ)"], "answer": "O(n²)", "difficulty": "medium"},
            {"q": "Overlapping subproblems means?", "options": ["Same subproblems solved repeatedly", "Each subproblem solved once", "Problems don't overlap", "Greedy works here"], "answer": "Same subproblems solved repeatedly", "difficulty": "medium"},
        ],
    },

    "Database Systems": {
        "SQL": [
            {"q": "Which SQL clause filters grouped results?", "options": ["WHERE", "HAVING", "GROUP BY", "ORDER BY"], "answer": "HAVING", "difficulty": "medium"},
            {"q": "What does JOIN do?", "options": ["Deletes rows", "Combines rows from two tables", "Creates a new table", "Filters columns"], "answer": "Combines rows from two tables", "difficulty": "easy"},
            {"q": "PRIMARY KEY constraint ensures?", "options": ["Unique + Not Null", "Only unique", "Only not null", "Foreign reference"], "answer": "Unique + Not Null", "difficulty": "easy"},
            {"q": "What is a subquery?", "options": ["A stored procedure", "A query inside another query", "A view", "An index"], "answer": "A query inside another query", "difficulty": "medium"},
            {"q": "ACID stands for?", "options": ["Atomicity, Consistency, Isolation, Durability", "Array, Class, Index, Data", "Access, Control, Input, Design", "None of these"], "answer": "Atomicity, Consistency, Isolation, Durability", "difficulty": "medium"},
        ],
        "Database Design": [
            {"q": "1NF requires?", "options": ["No partial dependencies", "Atomic column values", "No transitive dependencies", "A primary key only"], "answer": "Atomic column values", "difficulty": "medium"},
            {"q": "Foreign key creates a?", "options": ["Primary index", "Link between two tables", "Unique constraint", "View"], "answer": "Link between two tables", "difficulty": "easy"},
            {"q": "What is database normalization?", "options": ["Speeding up queries", "Reducing data redundancy", "Adding indexes", "Backing up data"], "answer": "Reducing data redundancy", "difficulty": "easy"},
            {"q": "An ER diagram represents?", "options": ["SQL queries", "Entities and relationships in a database", "Network topology", "UI flow"], "answer": "Entities and relationships in a database", "difficulty": "easy"},
            {"q": "3NF removes?", "options": ["Partial dependencies", "Transitive dependencies", "All dependencies", "Duplicate rows"], "answer": "Transitive dependencies", "difficulty": "hard"},
        ],
    },

    "Operating Systems": {
        "Processes & Threads": [
            {"q": "What is a process?", "options": ["A program on disk", "A program in execution", "A CPU register", "An OS file"], "answer": "A program in execution", "difficulty": "easy"},
            {"q": "Threads within same process share?", "options": ["Stack", "Registers", "Memory/heap", "Program counter"], "answer": "Memory/heap", "difficulty": "medium"},
            {"q": "Context switching involves?", "options": ["Saving and restoring process state", "Killing a process", "Creating a thread", "Memory allocation"], "answer": "Saving and restoring process state", "difficulty": "medium"},
            {"q": "What causes a deadlock?", "options": ["Too many threads", "Circular wait for resources", "High CPU usage", "Memory overflow"], "answer": "Circular wait for resources", "difficulty": "medium"},
            {"q": "Semaphore is used for?", "options": ["CPU scheduling", "Process synchronization", "Memory management", "File handling"], "answer": "Process synchronization", "difficulty": "medium"},
        ],
        "Memory Management": [
            {"q": "Virtual memory allows?", "options": ["Faster CPU", "Programs to use more memory than physically available", "Disk to act as CPU", "Network sharing"], "answer": "Programs to use more memory than physically available", "difficulty": "easy"},
            {"q": "Page fault occurs when?", "options": ["CPU overloads", "Required page not in RAM", "Disk is full", "Process terminates"], "answer": "Required page not in RAM", "difficulty": "medium"},
            {"q": "LRU page replacement replaces?", "options": ["Most recently used page", "Least recently used page", "Random page", "Oldest loaded page"], "answer": "Least recently used page", "difficulty": "easy"},
            {"q": "Thrashing means?", "options": ["High CPU utilization", "Excessive paging causing low CPU use", "Memory leak", "Cache overflow"], "answer": "Excessive paging causing low CPU use", "difficulty": "hard"},
            {"q": "Internal fragmentation occurs in?", "options": ["Segmentation", "Fixed-size partitioning", "Paging with variable size", "Virtual memory"], "answer": "Fixed-size partitioning", "difficulty": "hard"},
        ],
    },

    "Computer Networks": {
        "Network Basics": [
            {"q": "IP address works at which OSI layer?", "options": ["Layer 1", "Layer 2", "Layer 3", "Layer 4"], "answer": "Layer 3", "difficulty": "easy"},
            {"q": "TCP vs UDP — which is reliable?", "options": ["UDP", "TCP", "Both", "Neither"], "answer": "TCP", "difficulty": "easy"},
            {"q": "What does DNS do?", "options": ["Assigns IP addresses", "Translates domain names to IPs", "Encrypts traffic", "Routes packets"], "answer": "Translates domain names to IPs", "difficulty": "easy"},
            {"q": "HTTP runs on which port by default?", "options": ["21", "22", "80", "443"], "answer": "80", "difficulty": "easy"},
            {"q": "What is a subnet mask used for?", "options": ["Encrypting data", "Dividing network into subnetworks", "Assigning MAC address", "Routing between continents"], "answer": "Dividing network into subnetworks", "difficulty": "medium"},
        ],
        "Security": [
            {"q": "HTTPS uses which protocol for encryption?", "options": ["HTTP", "FTP", "TLS/SSL", "SSH"], "answer": "TLS/SSL", "difficulty": "easy"},
            {"q": "What is a Man-in-the-Middle attack?", "options": ["Flooding server", "Intercepting communication between two parties", "SQL injection", "Brute force"], "answer": "Intercepting communication between two parties", "difficulty": "medium"},
            {"q": "Firewall works by?", "options": ["Encrypting data", "Filtering network traffic by rules", "Compressing packets", "Assigning IPs"], "answer": "Filtering network traffic by rules", "difficulty": "easy"},
            {"q": "What is a DDoS attack?", "options": ["Data breach", "Overwhelming server with traffic", "Malware injection", "Password theft"], "answer": "Overwhelming server with traffic", "difficulty": "easy"},
            {"q": "Public key encryption uses?", "options": ["Same key to encrypt and decrypt", "Two keys — public to encrypt, private to decrypt", "Password only", "Shared secret"], "answer": "Two keys — public to encrypt, private to decrypt", "difficulty": "medium"},
        ],
    },

    "Mathematics": {
        "Linear Algebra": [
            {"q": "What is the dot product of orthogonal vectors?", "options": ["1", "-1", "0", "Undefined"], "answer": "0", "difficulty": "easy"},
            {"q": "Eigenvalues satisfy which equation?", "options": ["Av = λv", "Av = v", "A + v = λ", "det(A) = 0"], "answer": "Av = λv", "difficulty": "medium"},
            {"q": "A matrix with det = 0 is?", "options": ["Invertible", "Singular", "Diagonal", "Symmetric"], "answer": "Singular", "difficulty": "easy"},
            {"q": "PCA uses which decomposition?", "options": ["LU", "QR", "SVD / Eigendecomposition", "Cholesky"], "answer": "SVD / Eigendecomposition", "difficulty": "hard"},
            {"q": "Rank of a matrix is?", "options": ["Number of rows", "Number of columns", "Number of linearly independent rows/cols", "Determinant value"], "answer": "Number of linearly independent rows/cols", "difficulty": "medium"},
        ],
        "Probability & Statistics": [
            {"q": "P(A|B) means?", "options": ["P(A) divided by P(B)", "Probability of A given B occurred", "P(A) + P(B)", "P(A) × P(B)"], "answer": "Probability of A given B occurred", "difficulty": "easy"},
            {"q": "Standard deviation measures?", "options": ["Average value", "Spread of data", "Skewness", "Correlation"], "answer": "Spread of data", "difficulty": "easy"},
            {"q": "Bayes' theorem relates?", "options": ["Mean and variance", "Prior and posterior probability", "Two independent events", "Correlation and causation"], "answer": "Prior and posterior probability", "difficulty": "medium"},
            {"q": "Central Limit Theorem states?", "options": ["All data is normal", "Sample means approach normal distribution", "Variance is always 1", "Mean equals median"], "answer": "Sample means approach normal distribution", "difficulty": "medium"},
            {"q": "What is a p-value?", "options": ["Probability of the hypothesis being true", "Probability of observing results if null hypothesis is true", "Confidence interval width", "Effect size"], "answer": "Probability of observing results if null hypothesis is true", "difficulty": "hard"},
        ],
    },

    "Software Engineering": {
        "Design Patterns": [
            {"q": "Singleton pattern ensures?", "options": ["Multiple instances", "Only one instance of a class", "Fast creation", "Thread safety always"], "answer": "Only one instance of a class", "difficulty": "easy"},
            {"q": "Observer pattern is used for?", "options": ["Database access", "Event-driven communication", "Sorting", "Memory management"], "answer": "Event-driven communication", "difficulty": "medium"},
            {"q": "Factory pattern creates?", "options": ["Database connections", "Objects without specifying exact class", "UI components only", "Threads"], "answer": "Objects without specifying exact class", "difficulty": "medium"},
            {"q": "MVC stands for?", "options": ["Model View Controller", "Machine Virtual Component", "Main View Class", "Module Version Control"], "answer": "Model View Controller", "difficulty": "easy"},
            {"q": "SOLID — 'O' stands for?", "options": ["Open for modification", "Open/Closed Principle", "Object Orientation", "Output design"], "answer": "Open/Closed Principle", "difficulty": "hard"},
        ],
        "Version Control": [
            {"q": "git commit does?", "options": ["Pushes to remote", "Saves snapshot of staged changes", "Creates a branch", "Merges code"], "answer": "Saves snapshot of staged changes", "difficulty": "easy"},
            {"q": "git merge vs git rebase — what's the difference?", "options": ["Same thing", "Merge preserves history, rebase rewrites it", "Rebase is slower", "Merge deletes branches"], "answer": "Merge preserves history, rebase rewrites it", "difficulty": "hard"},
            {"q": "What is a pull request?", "options": ["Pulling latest changes", "Request to merge your branch into main", "Deleting a branch", "Cloning a repo"], "answer": "Request to merge your branch into main", "difficulty": "easy"},
            {"q": "git stash does?", "options": ["Deletes changes", "Temporarily saves uncommitted changes", "Commits everything", "Pushes to remote"], "answer": "Temporarily saves uncommitted changes", "difficulty": "medium"},
            {"q": ".gitignore is used to?", "options": ["Track all files", "Exclude files from being tracked", "Delete files", "Push files"], "answer": "Exclude files from being tracked", "difficulty": "easy"},
        ],
    },
}


def get_domains():
    return list(QUESTION_BANK.keys())


def get_topics(domain):
    return list(QUESTION_BANK.get(domain, {}).keys())


def get_questions(domain, topic):
    return QUESTION_BANK.get(domain, {}).get(topic, [])


def get_questions_by_difficulty(domain, topic, difficulty):
    all_q = get_questions(domain, topic)
    return [q for q in all_q if q["difficulty"] == difficulty]