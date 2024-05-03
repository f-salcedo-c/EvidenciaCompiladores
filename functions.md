# Script Functions

This lexer applies different functions to provide the use cases available.

`translator.py` provides the implementation of the grammar specified onto a lexer and parser in an interpreter. It utilizes the following functions to provide said work.

There are several functions that fall under the category of parse rules or tokenization rules: these are identified by a prefix `p_` or `t_` respectively. These give the rules necessary for the lexer to interpret inputs. Other functions include,

## add_node(attr)

Adds a node to the global parseGraph tree.

**Parameters:** 
- `attr`: Dictionary containing the node’s attributes.

**Returns:**
- The node at `NODE_COUNTER - 1`

## execute_parse_tree(tree)

Parses a tree and evaluates the value of each node.

**Parameters:** 
- `tree`: nx.Graph containing the tree to parse

**Returns:**
- Value of the evaluation

## visit_node(tree, node_id, from_id)

Visits a given node in a given tree and evaluates it.

**Parameters:** 
- `tree`: nx.Graph containing the tree
- `node_id`: Index of node to visit.
- `from_id`: Index of parent node.

**Returns:**
- Value of the evaluation

`library.py` is an appendix of predefined functions that interact with the numpy and OpenCV libraries; these predefined functions are accounted for in the lexer’s symbol table and are therefore usable in the lexer’s language.

## load_image(path)

Using OpenCV, takes an image and loads it.

**Parameters:** 
- `path`: String containing specified image path.

**Returns:**
- `np.ndarray`

## save_image(filename, image)

Using OpenCV, takes an np.ndarray and stores the image onto a file

**Parameters:** 
- `filename`: String containing specified output path.
- `image`: np.ndarray containing the image

**Returns:**
- None

## show_image(img)

Using OpenCV, displays the image onto a separate window

**Parameters:** 
- `img`: np.ndarray containing the image

**Returns:**
- Same type as img

## search_cv2(function_name)

Looks for a function by name under the CV2 library and returns it

**Parameters:** 
- `function_name`: Name of specified function

**Returns:**
- Value of `getattr`

## gen_matrix(a, b, *args)

Using NumPy, generates a fixed-size matrix filled with values.

**Parameters:** 
- `a`: Int specifying rows in matrix
- `b`: Int specifying columns in matrix
- `args`: Ordered values packed in a tuple

**Returns:**
- `np.ndarray`

## gen_vector(*args)

Using NumPy, generates a vector filled with values.

**Parameters:** 
- `args`: Ordered values packed in a tuple

**Returns:**
- `np.ndarray`

