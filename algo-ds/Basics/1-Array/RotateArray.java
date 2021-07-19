
public class RotateArray {

    static int[] rotateArray(int[] A, int K) {
        int length = A.length;
        // Return null if empty array
        if (length == 0) return null;

        int[] newRange = new int[length];
        // Change K to remainder, handel if rotation greater than length
        int rotation = K > length ? K % length : K;
        int pivot = length - rotation;

        for (int i = 0; i < length; i++) {
            newRange[i] = i < rotation ? length - rotation + i : pivot + i - length;
        }

        int[] rotatedArray = new int[length];
        for (int i = 0; i < length; i++) {
            rotatedArray[i] = A[newRange[i]];
        }
        // Return the Rotated array
        return rotatedArray;
    }

    public static void main(String[] args) throws Exception {
        rotateArray(new int[]{3, 8, 9, 7, 6}, 1);
    }

}