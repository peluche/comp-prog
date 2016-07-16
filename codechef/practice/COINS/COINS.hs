-- https://www.codechef.com/problems/COINS
import Data.Array
import qualified Data.Map as M
import Data.Maybe

-- bottom up DP is slow because the needed elems are sparse
solve_bot_up n = dp ! n
  where
    dp = listArray (0, n) (0 : map f [1..n])
    f i = max i (dp ! (i `quot` 4) + dp ! (i `quot` 3) + dp ! (i `quot` 2))


solve n = snd $ solve' (M.empty, n)
  where
    solve' (memo, 0) = (memo, 0)
    solve' (memo, n)
      | isJust memoM = (memo, fromJust memoM)
      | otherwise = (M.insert n res memo3, res)
      where memoM = M.lookup n memo
            (memo1, v1) = solve' (memo,  n `div` 4)
            (memo2, v2) = solve' (memo1, n `div` 3)
            (memo3, v3) = solve' (memo2, n `div` 2)
            res = max n (v1 + v2 + v3)
  
main = interact (unlines . map (show . solve . read) . lines)
