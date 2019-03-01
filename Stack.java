/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package stack;

/**
 *
 * @author Dylan
 */
public class Stack {
    private int top;
    private int[] arr;
    
    Stack (int size) {
        if (size <= 0 )
            System.out.print("Stack must be postive");
        else 
            arr = new int[size];
            top = -1;
    }

    void push (int x){
            top++;
            arr[top] = x;
    }
    
    int peek() {
        return arr[top];
    }
    
    void pop() {
        System.out.print(arr[top]);
        top--;
    }
    
    boolean isEmpty () {
            if (top == -1)
                return true;
            else return false;
    }
    public void print(){

        for(int i=0;i<=top;i++){
            System.out.print(arr[i]+ "  ");
        }
        System.out.println();
    }
                     
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Stack newStack = new Stack(4);
        newStack.push(17);
        newStack.push(8);
        newStack.push(2);
        newStack.push(3);
        
        newStack.print();
        newStack.pop();
        newStack.pop();
        newStack.pop();
        newStack.pop();
        newStack.print();
        
                              
        
        // TODO code application logic here
    }
    
}
