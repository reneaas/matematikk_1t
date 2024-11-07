

```{mermaid}
graph TD
    A["$$ax^2 + bx + c$$"]
    style A fill:#e0f7fa,stroke:#00796b,stroke-width:2px,shape:rect,font-size: 20px

    B["$$a(x - x_0)^2 + y_0$$"]
    style B fill:#ffecb3,stroke:#ff8f00,stroke-width:2px,shape:rect,font-size: 20px

    C["$$a(x - x_1)(x - x_2)$$"]
    style C fill:#ffccbc,stroke:#d84315,stroke-width:2px,shape:rect,font-size: 20px

    A -- "Fullstendig kvadraters metode" --> B
    B -- "Konjugatsetningen" --> C

```