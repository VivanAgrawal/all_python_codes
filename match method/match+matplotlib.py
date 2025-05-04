import matplotlib.pyplot as plt

graph = input("Enter graph type (line/bar/scatter/histogram/pie): ").strip().lower()

match graph:
    case "line" | "bar" | "scatter" | "histogram":
        x = list(map(float, input("Enter x values (comma separated): ").split(',')))
        y = list(map(float, input("Enter y values (comma separated): ").split(','))) if graph != "histogram" else None

        match graph:
            case "line":
                plt.plot(x, y)
            case "bar":
                plt.bar(x, y)
            case "scatter":
                plt.scatter(x, y)
            case "histogram":
                plt.hist(x, bins=10)
                

    case "pie":
        sizes = list(map(float, input("Enter values for pie chart (comma separated): ").split(',')))
        labels = input("Enter labels (comma separated): ").split(',')
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        
        
    case _:
        print("Invalid graph type")
        exit()

plt.title(f"{graph} Chart")
plt.show()
