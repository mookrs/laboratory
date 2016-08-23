/*
* Given an array of integers, return indices of the two numbers such that they add up to a specific target.
*
* You may assume that each input would have exactly one solution.
*
* Example:
* Given nums = [2, 7, 11, 15], target = 9,
*
* Because nums[0] + nums[1] = 2 + 7 = 9,
* return [0, 1].
*/

public class P1TwoSum {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] { i, j };
                }
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }

    public static void main(String[] args) {
        P1TwoSum solution = new P1TwoSum();

        int[] nums = { 2, 7, 11, 15 };
        int target = 9;

        int[] indexes = solution.twoSum(nums, target);
        System.out.println("[" + indexes[0] + ", " + indexes[1] + "]");
    }
}