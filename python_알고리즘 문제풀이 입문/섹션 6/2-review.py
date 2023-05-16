def preorder(n):
    if n >= 8:
        return
    else:
        print(n, end=' ')
        preorder(n * 2)
        preorder(n * 2 + 1)
        
def inorder(n):
    if n >= 8:
        return
    else:
        inorder(n * 2)
        print(n, end=' ')
        inorder(n * 2 + 1)
    
def postorder(n):
    if n >= 8:
        return
    else:
        postorder(n * 2)
        postorder(n * 2 + 1)
        print(n, end=' ')
    
preorder(1)
inorder(1)
postorder(1)