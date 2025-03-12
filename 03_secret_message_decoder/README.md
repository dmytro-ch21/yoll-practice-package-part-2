# 02_Secret_Message_Decoder

## Description

Write a program that decodes hidden messages. The decoder extracts characters at regular intervals (every nth character) to reveal the secret message.

## Background

Throughout history, simple cryptographic techniques have been used to hide messages in plain sight. This particular method (extracting every nth character) is a form of steganography — hiding a message within another message or medium.

## Instructions

1. Prompt the user to enter an encoded message with the following text:

   ```
   Enter the encoded message:
   ```

2. Prompt the user to enter the step size (an integer) for decoding:

   ```
   Enter the step size:
   ```

3. Extract every nth character from the message:

4. Print the decoded message:
   ```
   Decoded Message: [your_decoded_message]
   ```

## Examples

### Example 1:

```
Enter the encoded message: HH17GekrZblLSrvlxRpWoo[Df C*WrWZb>CoKp=&r(kpul1$7Sd:t6r!C4Lc
Enter the step size: 5
Decoded Message: Hello World!
```

### Example 2:

```
Enter the encoded message: BNb1e1bIlF2tix)Gei~*v0BNe=!N }{Ii2RqnU]t tnPybRhoLH6uWi2rK:?sezXemeslvC[f3,}.^)V
Enter the step size: 4
Decoded Message: Believe in yourself.
```

### Example 3:

```
Enter the encoded message: Wf=hEBa52t~@ -[gL(ek:tQas6C $HwHieM[tNHt6ee%;rrc jLa2ksvg N}iC2t@j yvdRBrc7i?)eq3sp}?xf
Enter the step size: 3
Decoded Message: What gets wetter as it dries?
```

### Example 4:

```
Enter the encoded message: Tza likJ ?iFsQ :c?hxeJaMp-.} sSWhwo4wP Ympe! _t3hMe} Nc.o;die@.& 9—U ALIi9n0uGsn 9Tmonrtv]a ludGs,
Enter the step size: 2
Decoded Message: Talk is cheap. Show me the code. — Linus Torvalds
```

## Tips

- String slicing syntax in Python: `string[start:end:step]`
- To get every nth character starting from index 0, use: `string[::n]` or `string[::n]`
- Remember that Python uses 0-based indexing, so the first character is at index 0
- The encoded messages in the examples contain hidden meaningful messages - try to figure them out!

> ### 😉 Hints:
>
> ---
>
> 1. You don't need `if` statements to handle input validation. Remember you can use logical operators (`and`, `or`) for short-circuit control flow!
>
> **Example**
>
> ```python
> is_valid = True
> is_valid or print("Error message")  # Only prints if is_valid is False
> ```
>
> ---

#### Secret Message Decoder Test Data

| Encoded Input                                                                                        | Step Size | Decoded Output                                      |
| ---------------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------- |
| `HH17GekrZblLSrvlxRpWoo[Df C*WrWZb>CoKp=&r(kpul1$7Sd:t6r!C4Lc`                                  | 5         | `Hhello World!`                                     |
| `BNb1e1bIlF2tix)Gei~*v0BNe=!N }{Ii2RqnU]t tnPybRhoLH6uWi2rK:?sezXemeslvC[f3,}.^)V`                   | 4         | `Believe in yourself.`                              |
| `Wf=hEBa52t~@ -[gL(ek:tQas6C $HwHieM[tNHt6ee%;rrc jLa2ksvg N}iC2t@j yvdRBrc7i?)eq3sp}?xf`            | 3         | `What gets wetter as it dries?`                     |
| `Tza likJ ?iFsQ :c?hxeJaMp-.} sSWhwo4wP Ympe! _t3hMe} Nc.o;die@.& 9—U ALIi9n0uGsn 9Tmonrtv]a ludGs,` | 2         | `Talk is cheap. Show me the code. — Linus Torvalds` |

### Message for you! - use your script to decode it 🚀

> `E>h0Ovoo#sevJ^erVpvmy6Rr( RCIQl%MbBiD;qDnBZpWeeo(9 %&0KocnOSfzA+( $)h.c^@djo_lV)d8WYheu)A6 TggXbUq!Au1O?>i!xwwl4S4CdM2CRsu][S {;Ysy{Gupot712uQ}%frLnp@ ^KX<f BhDu#{:bt5RD~uo>8.rLK~YeKvKA.aFt? x(_3MegGtidzgGsXdErt~>m{a&w]ykmUK5e&;w;s]#z^ a>m%h-r1ue.GM%lD*DnpTAX@ aQ>ZyJop<oaD*&uUWw6 8_DZlq$xde6A7SaM=*Arj=-vntb[[.Ni Z pSb&K4d^ue_p2meK&]+p4}Ru %IP^cAvD0oR;QId$-[ri^;KvnDZQ-g5poN ^@xGaI$4+n5V *dhVMY @p7=egNi8n7?;8j=d!4os).fy&Hc[ oR+&t5aaDh{Q.ne^XrT >K1PjgpZYoP18luz(J^r+cRDnIsn0e)8gSyAi4n!aOSy` - step 4
