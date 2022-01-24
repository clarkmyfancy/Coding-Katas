module Main where

import Test.Tasty
import Test.Tasty.HUnit

import Translator

main :: IO ()
main = defaultMain testRoot

testRoot :: TestTree
testRoot = testGroup "Translator" [
    translatorTests, 
    containsTheNumber3Tests, 
    containsTheNumber5Tests ]

translatorTests :: TestTree
translatorTests = testGroup ".translate"
    [
        testCase "when given 0, returns empty list" $
            translate 0 @?= []

        , testCase "when given 1, returns \"1\"" $
            translate 1 @?= "1"

        , testCase "when given 3, returns \"Fixx\"" $
            translate 3 @?= "Fixx"

        , testCase "when given 5, returns \"Bucks\"" $
            translate 5 @?= "Bucks"

        , testCase "when given second multiple of 3, returns \"Fixx\"" $
            translate 6 @?= "Fixx"
        
        , testCase "when given second multiple of 5, returns \"Bucks\"" $
            translate 10 @?= "Bucks"
        
        , testCase "when given a multiple of both 3 AND 5, returns \"FixxBucks\"" $
            translate 15 @?= "FixxBucks"
    ]

containsTheNumber3Tests :: TestTree
containsTheNumber3Tests = testGroup ".containsTheNumber (comparing with 3)"
    [
        testCase "when given 0, returns False" $
            0 `containsTheNumber` 3 @?= False

        , testCase "when given 24542897492, returns False" $
            24542897492 `containsTheNumber` 3 @?= False
        
        , testCase "when given 3, returns True" $
            3 `containsTheNumber` 3 @?= True
                
        , testCase "when given 153450000, returns True" $
            153450000 `containsTheNumber` 3 @?= True
    ]

containsTheNumber5Tests :: TestTree
containsTheNumber5Tests = testGroup ".containsTheNumber (comparing with 5)"
    [
        testCase "when given 0, returns False" $
            0 `containsTheNumber` 5 @?= False

        , testCase "when given 200442897492, returns False" $
            200442897492 `containsTheNumber` 5 @?= False
        
        , testCase "when given 5, returns True" $
            5 `containsTheNumber` 5 @?= True
                
        , testCase "when given 153450000, returns True" $
            153450000 `containsTheNumber` 5 @?= True
    ]