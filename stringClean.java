package com.google.challenges; 

public class Answer {   
    public static String answer(String chunk, String word) { 

    if (compareString(chunk, word)) return "";
    String s1 = checkBack(chunk, word);
    String s2 = checkFront(chunk, word);
    
    return calculateLexi(s1,s2);
    
    }
    
    private static String calculateLexi(String s1, String s2)
    {
        //return name1.compareTo(name2);
                int ls1 = s1.length();
                int ls2 = s2.length();
                int len = ls1 > ls2 ? ls2 : ls1;
                for(int i = 0; i < len; i++){
                    int lexcompare1 = s1.charAt(i);
                    int lexcompare2 = s2.charAt(i);
                    if(lexcompare2 > lexcompare1) {
                        return s1;
                    } else if (lexcompare1 > lexcompare2) {
                        return s2;
                    }
                }
                return s1;
    }

    private static String checkBack(String chunk, String word)
    {
        if (compareString(chunk, word)) return "";
        if (chunk.length() <= word.length()) return chunk;
        for (int i = chunk.length(); i >= word.length(); i--)
        {
            if (compareString(chunk.substring(i-word.length(), i), word))
            {
                String s1 = checkFront(removeAt(i-word.length(), i-1, chunk), word);
                String s2 = checkBack(removeAt(i-word.length(), i-1, chunk), word);
                return calculateLexi(s1,s2);
            }
        }
        return chunk;
    }
    
    private static String checkFront(String chunk, String word)
    {
        if (compareString(chunk, word)) return "";
        if (chunk.length() <= word.length()) return chunk;
        for (int i = 0; i < chunk.length()-word.length(); i++)
        {
            if (compareString(chunk.substring(i, word.length()+i), word))
            {
                String s1 = checkFront(removeAt(i, word.length()+i-1, chunk), word);
                String s2 = checkBack(removeAt(i, word.length()+i-1, chunk), word);
                return calculateLexi(s1,s2);
              
            }
        }
        return chunk;
    }
    
    private static String removeAt(int startIndex, int endIndex, String input)
    {
       if (endIndex+1 == input.length())
       {
           return input.substring(0, startIndex);
       }
       else 
       {
          return input.substring(0, startIndex) + input.substring(endIndex+1);
       }
     }
    
     private static boolean compareString(String s1, String s2)
     {
       char[] c1 = s1.toCharArray();
       char[] c2 = s2.toCharArray();
       if (c1.length != c2.length) return false;
       for (int i = 0; i < c1.length; i++)
       {
           if (c1[i] != c2[i]) return false;      
       }
       return true;
     }
}
