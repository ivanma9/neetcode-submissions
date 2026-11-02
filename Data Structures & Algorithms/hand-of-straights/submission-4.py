class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        obs:
            if not divisible by groupsize false
            cards have to be consecutive
            duplicates possible
        goal
            t/f if possible to group

        approach 1:
            find earlest start then try to make a streak of group size then. if already "used", cannot use again
            use hm to do glossary
            if streak lets mark all as used. if streak is not possible return false, those cards never find another partner

        '''
        if len(hand) % groupSize != 0:
            return False
        cards = Counter(hand)
        cards_used = 0
        for j in hand:
            if j not in cards or cards[j] == 0:
                continue
            card = j
            while(card in cards and cards[card] > 0): #O(n)
                card-=1
            card = card+1
            # lowest card in streak

            #mark as we go
            # print(card, cards)
            for i in range(card,card+groupSize): #O(groupSize)
                if i in cards and cards[i] >0:
                    cards[i] -=1
                else:
                    return False
            cards_used += groupSize
            if cards_used == len(hand):
                return True
        return True
                
