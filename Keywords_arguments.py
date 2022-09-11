def say_hey(Name, msg="what are you doing?"):
    print("hi", Name +"," + msg)


say_hey(Name="kati", msg="Good Morning!")
say_hey(msg="Good Morning!", Name="kati")
say_hey("kati", msg="Good Morning!")
say_hey("Good Morning!","kati")
