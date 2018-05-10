function Node(val){
    this.val = val;
    this.left = null;
    this.right = null;
}

function inOrder(head){
    
    let current = head, 
        stack = [], result = [],
        isDone = false;
    

    // create a stack for backtracking
    while(!isDone){  
        // if there is nothing in stack also no next left node nor right node
        // then stop
        if(current){
            // store current in stack for backtracking later
            stack.push(current)

            // keep dive into left node
            current = current.left;
        }else{
            
            // if there is no left node, then backtracking from stack
            if(stack.length > 0){
                // let current be the last node we just put into stack
                // and remove it from stack
                current = stack.pop();
                
                //record current node
                result.push(current.val);

                // reassign current node to its right node 
                current = current.right;

            }else{
                // if there is no nodes on stacks then we can stop traverse
                isDone = true;
            }
        }
    }
   
    return result;
}


let head = new Node(1);
head.left = new Node(2);
head.right = new Node(3);
head.left.left = new Node(4);
head.left.right = new Node(5);
console.log('head', head);
console.log(inOrder(head));
