module Console where

import Translator

printHeader :: IO() 
printHeader = do
    printNBlankLines 3
    putStrLn "__________________________"
    putStrLn "         welcome          "
    putStrLn "       to FixxBucks       "

printNBlankLines :: Int -> IO()
printNBlankLines 0 = putStr ""
printNBlankLines n = do 
    putStr "\n"
    printNBlankLines (n - 1)

showUpperBoundPrompt :: IO() 
showUpperBoundPrompt = putStr "what is the upper bound?  -> "

getUpperBoundAndDeriveResults :: IO()
getUpperBoundAndDeriveResults = do 
    upperBound <- getLine
    printNBlankLines 1
    printTranslation (read upperBound :: Int)

printTranslation :: Int -> IO()
printTranslation upperBound = do 
    explainWhatWillHappenWith upperBound
    envokeTranslator [1..upperBound]

explainWhatWillHappenWith :: Int -> IO()
explainWhatWillHappenWith upperBound = do 
    putStr ("running FixxBucks with the numbers 1 through " ++ show upperBound)
    printNBlankLines 1

envokeTranslator :: [Int] -> IO()
envokeTranslator [] = printNBlankLines 1
envokeTranslator (x:xs) = do
    putStrLn (show x ++ ":  " ++ translate x)
    envokeTranslator xs