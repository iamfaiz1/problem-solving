public class CheckSorted {
    public static boolean isSorted(int[] arr, int n, int i){
        if (i>=n-1) return true;

        if (arr[i]<= arr[i+1]) return isSorted(arr, n, i+1);
        else return false;
    }
    public static void main(String[] args) {
        int []arr = {1, 2, 4, 5, 6, 10, 11, 100};
        int []arr2 = {1, 2, 40, 5, 6, 10, 11, 100};
        
        System.out.println(CheckSorted.isSorted(arr, arr.length, 0));
        System.out.println(CheckSorted.isSorted(arr2, arr2.length, 0));
    }
}
