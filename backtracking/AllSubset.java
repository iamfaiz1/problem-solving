import java.util.ArrayList;

public class AllSubset {
    public static void subset(int [] arr, int i ,ArrayList<Integer> a2){
        // backtracking
        if(i>=arr.length){
            System.err.println(a2);
            return;
        }
        // including case
        a2.add(arr[i]);
        subset(arr, i+1, a2);

        // excluding case
        a2.remove(a2.size() - 1);
        subset(arr, i+1, a2);

    }

    public static void main(String[] args) {
        int [] arr = {1, 2, 3};
        subset(arr, 0, new ArrayList<Integer>());
    }
}
