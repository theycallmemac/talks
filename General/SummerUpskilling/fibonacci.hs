module Main where

fibonacci :: Int -> Int
fibonacci 0 = 1
fibonacci 1 = 1
fibonacci n = fibonacci(n - 1) + fibonacci(n - 2)

main = do
    input <- getLine
    print . fibonacci . (read :: String -> Int) $ input
