# Database Design

## Functional Dependencies

是一种决定关系

### Canonical Cover（正则覆盖）

```sql
To compute a canonical cover for F:
repeat
    Use the union rule to replace any dependencies in F like α1 → β1 and α1 → β2 with α1 → β1 β2
    Find a functional dependency α → β with an
        extraneous attribute either in α or in β
    If an extraneous attribute is found, delete it
        from α → β
until F does not change
```

## Decomposition

### Lossless

无损连接分解的条件：
分解后的二个子模式的共同属性必须是R1或R2的码。（适用于一分为二的分解）

### Dependency Preservation

\((F_1 \cup F_2 \cup ... \cup F_n)^+ = F^+\)

**TEST**

Algorithm to test if a dependency α → β is preserved:

```sql
result = α
while (changes to result) do
    for each Ri in the decomposition
        t = (result ∩ Ri)+ ∩ Ri
        result = result ∪ t

If result contains all attributes in β, 
    then the functional dependency α → β is preserved.
```

Apply the test on all dependencies in F to check if a decomposition is dependency preserving.

## Boyce-Codd Normal Form

For all α → β in F+, where α ⊆ R and β ⊆ R, one of these conditions must hold:
- α → β is trivial (i.e., β ⊆ α)
- α is a superkey for R (i.e., R ⊆ α+, α → R)

To check if a relation schema R is in BCNF, it suffices to check only the dependencies in the given set F for violation of BCNF, rather than checking all dependencies in F+.  
(可在F下判别R是否违反BCNF，但须在F+下判别R的分解式是否违反BCNF.)

### BCNF Decomposition Algorithm

```sql
result := {R};
done := false;
compute F+;
while (not done) do
    if (there is a schema Ri in result that is not in BCNF)
        then begin
            let α → β be a nontrivial functional dependency that holds on Ri
                such that α → Ri is not in F+,
                and α ∩ β = ∅;
            result := (result - Ri) ∪ (α, β) ∪ (Ri - β);
        end
    else done := true;
Note: at last, every sub-schema is in BCNF, and the decomposition is lossless-join.
```
将Ri分解为两个子模式：Ri1=(α, β)和Ri2=(Ri - β)，其中α是Ri1和Ri2的共同属性

## Third Normal Form

For all α → β in F+, where α ⊆ R and β ⊆ R, one of these conditions must hold:
- α → β is trivial (i.e., β ⊆ α)
- α is a superkey for R (i.e., R ⊆ α+, α → R)
- Each attribute A in α - β is contained in a candidate key for R.

### TNF Decomposition Algorithm

```sql
Let Fc be a canonical cover for F;
i := 0;
for each functional dependency α → β in Fc do {
    if none of the schemas Rj, 1 ≤ j ≤ i contains α β
        then begin
            i := i + 1;
            Ri := (α β)
        end}
if none of the schemas Rj, 1 ≤ j ≤ i contains a
candidate key for R then begin
    i := i + 1;
    Ri := any candidate key for R;
end
return (R1, R2, ..., Ri)
```

## Fourth Normal Form

引入了 multi-valued dependency，trivial 的条件多了一条 $\alpha\cup\beta = R_i$ 其他跟 BCNF 一样

$\twoheadrightarrow$
