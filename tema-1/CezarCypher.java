class CezarCypher {

    public static StringBuffer encrypt(String text, int s)
    {
        StringBuffer result= new StringBuffer();
 
        for (int i=0; i<text.length(); i++)
        {
            if (Character.isUpperCase(text.charAt(i)))
            {
                char ch = (char)(((int)text.charAt(i) +
                                  s - 65) % 26 + 65);
                result.append(ch);
            }
            else
            {
                char ch = (char)(((int)text.charAt(i) +
                                  s - 97) % 26 + 97);
                result.append(ch);
            }
        }
        return result;
    }

    private static void getVariants(String message) {
        for(int key = 1; key <= 25; key++){
            System.out.println("Key:" + key);
            System.out.println("Cipher: " + encrypt(message, key));
        }
    }

    public static void main(String args[]) {
        switch(args.length) {
            case 1:
                getVariants(args[0]);
                break;
            default:
                System.out.println("Too many or No args");
                break;

        }
    }
}