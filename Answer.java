package com.google.challenges; 
import java.util.*;

public class Answer {   
    public static String[] answer(String[] names) { 

        // Your code goes here.
        //String[] sorted =  new String[names.length];
       // int counter = 0;
        
        //while((counter) < names.length)
        //{
         //   String temp = findBiggest(names);
         //   sorted[counter] = temp;
         //   counter ++ ;
        //}
        
        //for(int i = 0; i < sorted.length; i++)
        //{
          //   System.out.println(sorted[i]);
        //}
        Arrays.sort(names, new scoreComparator());

        return names;

    } 
    
    private static class scoreComparator implements java.util.Comparator<String> {
        @Override
        public int compare(String s1, String s2) {
            int val1 = calculateScore(s1);
            int val2 = calculateScore(s2);
            if(val1 > val2)
                return -1;

            if(val2 > val1)
                return 1;

            // Handles the same score case and compares for the lexicographically larger name.
            if(val1 == val2){
                return calculateLexi(s1,s2);
            }

            return 0;
        }
    }
    
    public static String findBiggest(String[] names)
    {
        String max = "";
        int index = 0;
        for (int i = 1; i < names.length; i++) {
            if (calculateScore(names[i]) >= calculateScore(max)) {
               
               if(calculateLexi(names[i], max)<0)
                    {   
                        max = names[i];
                        index  = i;
                        
                    }
            }
        }
        names[index] = "";
        return max;
    }
    
    
    public static int calculateScore(String name)
    {
        int sum = 0;
        for (char c : name.toCharArray()) {
            sum = sum + (c - 'a' + 1);
        }
        return sum;
    }
    
    public static int calculateLexi(String s1, String s2)
    {
        //return name1.compareTo(name2);
                int ls1 = s1.length();
                int ls2 = s2.length();
                int len = ls1 > ls2 ? ls2 : ls1;
                for(int i = 0; i < len; i++){
                    int lexcompare1 = s1.charAt(i);
                    int lexcompare2 = s2.charAt(i);
                    if(lexcompare2 > lexcompare1) {
                        return 1;
                    } else if (lexcompare1 > lexcompare2) {
                        return -1;
                    }
                }
    }
}
