def arithmetic_arranger(problems, show_answers=False):
    
    if len(problems)>5:
        return 'Error: Too many problems.'
    
    Upper=[]
    operator=[]
    Lower=[]
    Dash=[]
    Answer=[]
    
    #below splits the original list and appends to the above three lists
    for i in problems:
        split=i.split(' ')
        
        if split[1]!='-' and split[1]!='+':
            return "Error: Operator must be '+' or '-'."
        elif split[0].isdigit()==False or split[2].isdigit()==False:
            return "Error: Numbers must only contain digits."
        elif len(split[0])>4 or len(split[2])>4 :
            return 'Error: Numbers cannot be more than four digits.'
        else:
            Upper.append(split[0])
            operator.append(split[1])
            Lower.append(split[2])
        
        del split
    

    for i in range(len(Upper)):
        
        Dash.append('-'*(2+max(len(Upper[i]),len(Lower[i]))))

        if len(Upper[i])>len(Lower[i]):
            Lower[i]= operator[i]+(abs(len(Upper[i])-len(Lower[i]))+1)*' '+Lower[i]
            Upper[i]= 2*' '+Upper[i]
            
        elif len(Upper[i])<len(Lower[i]):
            Upper[i]= (abs(len(Upper[i])-len(Lower[i]))+2)*' '+Upper[i]
            Lower[i]= operator[i]+' '+Lower[i]
        
        else:
            Upper[i]= 2*' '+Upper[i]
            Lower[i]= operator[i]+' '+Lower[i]


    if show_answers:
        for i,o in enumerate(operator):
            if o=='+':
                A=str(int(Upper[i][1:])+int(Lower[i][1:]))
            else:
                A=str(int(Upper[i][1:])-int(Lower[i][1:]))
            if i>0:
                Answer.append(' '*4 +(len(Dash[i])-len(A))*' '+A)
            else:
                Answer.append((len(Dash[i])-len(A))*' '+A)
        Upper   ='    '.join(Upper)
        Lower   ='    '.join(Lower)
        Dash    ='    '.join(Dash)
        Answer  =''.join(Answer)
        Problem =Upper+'\n'+Lower+'\n'+Dash+'\n'+Answer
    else:
        Upper   ='    '.join(Upper)
        Lower   ='    '.join(Lower)
        Dash    ='    '.join(Dash)
        Problem =Upper+'\n'+Lower+'\n'+Dash

    return Problem


# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])