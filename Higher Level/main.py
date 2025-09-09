questions = [
    ["Compare Youtubers Total Gaming Vs Amit Gaming",1],
    ["Which app is most banned in countries Tik tok vs x(Twitter)",1],
    ["Which is Better For Gaming Asus vs Razer vs Hp",2],
    ["Which Platform has more downloads chatgpt vs chrome",2],
    ["Which Country has More Gdp India vs Pakistan",1],
    ["Which games has more active users Bgmi or Free Fire",2],
    ["Which Leader Has More Popularity Narendra Modi vs Rahul Gandhi",1],
    ["Which Has More Youtube Subs Abp News vs Aaj Tak",2],
    ["Which Scientist is Intelligent Nicola Tesla vs Elbert Ienstien",1],
    ["Who is Popular Elon Musk vs Bill Gates",1],
    ["Which Language is Better for Systems Programming C++ vs Rust",2],
    ["Which Has Better Concurrency Model Go vs Node.js",1],
    ["Which Language Has Faster Compilation Time C++ vs D",2],
    ["Which Is More Functional Scala vs Kotlin",1],
    ["Which Language Has More Low-Level Memory Control C vs Assembly",2],
    ["Which Database Offers Better Horizontal Scalability MongoDB vs PostgreSQL",1],
    ["Which Programming Paradigm is Used More in Haskell vs Java",1],
    ["Which Is Better for Real-Time Applications Erlang vs Python",1],
    ["Which Language is More Popular for Data Science Python vs Julia",1],
    ["Which Language Supports Pattern Matching Better Elixir vs Ruby",1],
    ["Which Compiler is Faster Clang vs GCC",1],
    ["Which Has Better Type Inference Rust vs TypeScript",1],
    ["Which Framework is Faster for Web APIs FastAPI vs Django",1],
    ["Which Language Handles Null Safety Better Kotlin vs Java",1],
    ["Which Has Better GPU Support PyTorch vs TensorFlow",2],
    ["Which Has Better Static Typing Haskell vs Python",1],
    ["Which Is More Secure by Design Rust vs C",1],
    ["Which IDE Offers Better C++ Support Visual Studio vs Eclipse",1],
    ["Which Programming Language is More Verbose Java vs Go",1],
    ["Which Language Has More Built-in Support for Metaprogramming Lisp vs C#",1],
]
score = 0
run = 1
while run!=0:
    for question in questions:
        if score == 30:
            print("You won This Game 🎉🎉")
            run = 0
            break
        else:
            print(question[0])
            choice = int(input("Enter The choice:\n"))
            if choice == question[1]:
                score += 1
                print(f"You are correct score = {score}")
            elif choice != questions[1]:
                print("You are wrong!")
                run = 0
                break
