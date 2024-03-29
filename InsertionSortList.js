var insertionSortList = function(head) {
    
    if (head == null || head.next == null) return head;
    let dummy = new ListNode(head.val, head);
    let prev = dummy,
        cur = head;
    while (cur != null) {
        if (prev.val <= cur.val) {
            prev = cur;
            cur = cur.next;
            continue;
        }
        let p = dummy;
        while (p.next.val <= cur.val) {
            p = p.next;
        }
        let t = cur.next;
        cur.next = p.next;
        p.next = cur;
        prev.next = t;
        cur = t;
    }
    return dummy.next;
};
    
