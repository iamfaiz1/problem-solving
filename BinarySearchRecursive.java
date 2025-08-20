public class BinarySearchRecursive {
    public static int bSearch(int [] arr, int key){
        return find(arr, 0, arr.length-1, key);
    }

    public static int find(int []arr, int low, int high, int key){
            int mid;
            if(high<low) return -1;

            mid = low + (high-low)/2;

            if(arr[mid] == key) return mid;   
            else if(arr[mid] > key) return find(arr, mid-1, low, key) ;  
            else return find(arr, mid+1, high, key);    
    }

    public static void main(String[] args) {
        int []arr = {1, 2, 4, 5, 6, 10, 11, 100};
        int key = 10;
        int key2 = 3;

        System.out.println(BinarySearchRecursive.bSearch(arr, key)); // Should return index of key
        System.out.println(BinarySearchRecursive.bSearch(arr, key2)); // Should return -1 as key is not present
    }
}
