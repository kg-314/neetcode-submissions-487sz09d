/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head;
        ListNode cur;
        if (list1 == null) {
            return list2;
        } else if (list2 == null) {
            return list1;
        }
        
        if (list1.val < list2.val) {
            head = list1;
            list1 = list1.next;
        } else {
            head = list2;
            list2 = list2.next;
        }

        cur = head;

        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                ListNode temp = list1.next;
                cur.next = list1;
                cur = cur.next;
                list1 = temp;
            } else {
                ListNode temp = list2.next;
                cur.next = list2;
                cur = cur.next;
                list2 = temp;
            }
        }

        if (list1 == null) {
            while (list2 != null) {
                ListNode temp = list2.next;
                cur.next = list2;
                cur = cur.next;
                list2 = temp;
            }
        } else if (list2 == null) {
            while (list1 != null) {
                ListNode temp = list1.next;
                cur.next = list1;
                cur = cur.next;
                list1 = temp;
            }
        }

        return head;

    }
}