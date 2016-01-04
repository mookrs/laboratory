/*
* Given an array of integers, find two numbers such that they add up to a specific target number.
*
* The function twoSum should return indices of the two numbers such that they add up to the target, where index1 * must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
*
* You may assume that each input would have exactly one solution.
*
* Input: numbers={2, 7, 11, 15}, target=9
* Output: index1=1, index2=2
*/

public class P1TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];

        for (int i = 0; i < nums.length; i++) {
            for (int j = i; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    result[0] = i;
                    result[1] = j;
                    return result;
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        P1TwoSum solution = new P1TwoSum();

        int[] numbers = { 2, 7, 11, 15 };
        int target = 9;

        int[] indexes = new int[2];

        indexes = solution.twoSum(numbers, target);

        System.out.println("index1=" + indexes[0] + ", index2=" + indexes[1]);
    }
}