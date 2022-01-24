module Main where

import Console

main :: IO ()
main = do 
    printHeader
    printNBlankLines 1
    showUpperBoundPrompt
    getUpperBoundAndDeriveResults
    