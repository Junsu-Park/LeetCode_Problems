/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1==nullptr or list2==nullptr)
            return list1==nullptr ? list2 : list1;
        
        ListNode* Node_tmp;
        ListNode* ans;
        if(list1->val <= list2->val){
            Node_tmp = list1;
            ans = list1;
            list1 = list1->next;
        }
        else{
            Node_tmp = list2;
            ans = list2;
            list2 = list2->next;
        }
        while(list1!=nullptr and list2!=nullptr){
            if(list1->val <= list2->val){
                Node_tmp->next = list1;
                Node_tmp = Node_tmp->next;
                list1 = list1->next;
            }
            else{
                Node_tmp->next = list2;
                Node_tmp = Node_tmp->next;
                list2 = list2->next;
            }
        }
        if(list1==nullptr)
            Node_tmp->next = list2;
        else
            Node_tmp->next = list1;
        
        return ans;
    }
    
};