module Translator where

translate :: Int -> [Char]
translate 0 = []
translate num =
    let translation = attemptToAssignFixxTo num ++ attemptToAssignBucksTo num in    
        if translation /= ""
            then translation
        else show num

attemptToAssignFixxTo :: Int -> [Char]
attemptToAssignFixxTo x = do 
    if x `isEvenlyDivisibleBy` 3 
        || x `containsTheNumber` 3
        then "Fixx"
    else ""

attemptToAssignBucksTo :: Int -> [Char]
attemptToAssignBucksTo x = do 
    if x `isEvenlyDivisibleBy` 5 
        || x `containsTheNumber` 5
        then "Bucks"
    else ""

isEvenlyDivisibleBy :: Int -> Int -> Bool
isEvenlyDivisibleBy n d = n `mod` d == 0

containsTheNumber :: Int -> Int -> Bool
containsTheNumber 0 _ = False
containsTheNumber candidate comparator = 
    let valueOfRightMostDigit = candidate `mod` 10 in 
        if valueOfRightMostDigit == comparator
            then True
        else containsTheNumber (candidate `quot` 10) comparator

