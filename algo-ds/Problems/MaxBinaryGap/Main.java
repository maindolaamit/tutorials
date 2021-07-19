/**
 * A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
 * <p>
 * For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.
 * <p>
 * Write a function:
 * <p>
 * class Solution { public int solution(int N); }
 * <p>
 * that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
 * <p>
 * For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
 * <p>
 * Write an efficient algorithm for the following assumptions:
 * <p>
 * N is an integer within the range [1..2,147,483,647].
 **/
public class Main {

    private static int maxBinaryGap(String binary) {
        // If no binary gap present
        if (!binary.contains("0")) return 0;
        if (!binary.substring(1).contains("1")) return 0;

        char[] array = binary.toCharArray();
        int length, j, maxLength = 0, arrayLength = array.length;
        for (int i = 0; i < arrayLength; i++) {
            if (array[i] == '0') {
                // Loop till you encounter 1
                j = i;
                while (array[j] != '1') {
                    j++;
                    if (j == arrayLength) break;
                }
                // Return max length
                if (j == arrayLength && array[j - 1] != '1') {
                    return maxLength;
                } else {
                    // Compute length
                    length = j - i;
                    i = j;
                    if (length > maxLength) { maxLength = length;}
                }
            }
        }
        return maxLength;
    }

    public static void main(String[] args) throws Exception {
        int number = 32;
        String binary = Integer.toBinaryString(number);
        maxBinaryGap(binary)
    }

}