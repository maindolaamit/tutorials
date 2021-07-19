package com.company;

public class ArrayOperations {
    private int[] list;
    private int occupiedLength;

    public ArrayOperations(int[] values) {
        this.list = values;
        this.occupiedLength = values.length;
    }

    public ArrayOperations() {
        this.list = new int[5];
        this.occupiedLength = 0;
    }

    /**
     * Method to Print the values in the List
     */
    void print() {
        StringBuilder output = new StringBuilder();
        output.append("{");
        if (this.occupiedLength > 0) {
            for (int i = 0; i < this.occupiedLength; i++) {
                if (i > 0) {
                    output.append(",");
                }
                output.append(this.list[i]);
            }
        } else {
            output.append("List is Empty");
        }
        output.append("}");
        output.append(" - ").append(this.occupiedLength);
        System.out.println(output.toString());
    }

    private void extendList() {
        // Create  a new Array of twice size
        int[] a = new int[this.list.length * 2];
        // Loop over each element and copy
        for (int i = 0; i < this.list.length; i++) {
            a[i] = this.list[i];
        }
        this.list = a;
        System.out.println("List extended");
    }

    /**
     * Method to Insert an element at the given position
     *
     * @param pos position at which to insert, will be 1 more than Index
     */
    void insertAt(int pos, int value) {
        for (int i = this.occupiedLength - 1; i >= pos; i--) {
            this.list[i + 1] = this.list[i];
        }
        this.list[pos] = value;
        this.occupiedLength += 1;
    }

    /**
     * Method to insert a new value in the List
     *
     * @param value value to be inserted
     */
    void insert(int value) {
        // Check if array has become full
        if (this.list.length == this.occupiedLength) {
            extendList(); // Extended the array
        }
        this.list[occupiedLength] = value;
        this.occupiedLength += 1;
    }

    /**
     * Remove an element at the given Index
     *
     * @param pos
     */
    void removeAt(int pos) {
        if (pos <= this.occupiedLength) {
            for (int i = pos; i <= this.occupiedLength - 1; i++) {
                if (i + 1 == this.list.length) {
                    this.list[i] = 0;
                } else {
                    this.list[i] = this.list[i + 1];
                }
            }
            this.occupiedLength -= 1;
        } else {
            System.out.println(String.format("Invalid index %d : Maximum : %d", pos, this.occupiedLength));
        }
    }

    /**
     * Method to remove a value from the List
     *
     * @param value value to be removed
     */
    void remove(int value) {
        for (int i = 0; i < occupiedLength; i++) {
            if (value == this.list[i]) {
                removeAt(i);
                System.out.println(String.format("Removed %d", value));
                return;
            }
        }
        System.out.println(String.format("Value not in the List  : %d", value));
    }

    /**
     * An array A consisting of N integers is given. Rotation of the array means that each element is shifted right
     * by one index, and the last element of the array is moved to the first place. For example, the rotation of
     * array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).
     * <p>
     * The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.
     * <p>
     * View problem at below link
     * https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
     **/
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
}
