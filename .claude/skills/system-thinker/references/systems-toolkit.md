# Systems Toolkit

Contents:
1. The iceberg (four levels of a problem)
2. Stocks, flows, and delays
3. Loop notation and a worked example
4. The eight archetypes
5. Leverage points
6. Starter breakdowns for common business problems

## 1. The iceberg

Every problem can be read at four levels. Deeper levels give more leverage.

| Level | Question | Example |
|---|---|---|
| Event | What happened? | A key salesperson quit. |
| Pattern | What has been happening over time? | Four salespeople quit in 18 months, each around month 10. |
| Structure | What causes the pattern? | Commission is paid only after the customer's first year, so the first payout arrives late and small. |
| Belief | What assumption keeps the structure in place? | "Good salespeople are motivated by the long term." |

Fixing the event (hire a replacement) changes nothing. Fixing the structure or the belief stops the pattern.

## 2. Stocks, flows, and delays

- A **stock** is something that accumulates: cash, customers, inventory, staff, trust, skills, backlog.
- A **flow** fills or drains a stock: sales, churn, hiring, resignations.
- A **delay** is the gap between an action and its effect.

Use the bathtub picture: the water level (stock) changes only through the tap and the drain (flows). You cannot change a stock directly. "We need more customers" means: raise the inflow (acquisition) or lower the outflow (churn). Always ask which is cheaper.

Delays cause overreaction. If hiring takes four months to show in output, a manager who sees no result in month two hires again, and by month six the team is overstaffed. Name the delay and tell the user how long to wait before judging.

## 3. Loop notation

Write cause and effect as arrows.

- `A -> (+) B` means when A rises, B rises (they move the same way).
- `A -> (-) B` means when A rises, B falls (they move opposite ways).
- `||` on an arrow marks a delay.
- **R** = reinforcing loop: it amplifies change, in either direction (growth or collapse).
- **B** = balancing loop: it pushes back towards a limit or target.

To tell them apart, count the `(-)` arrows in the loop. An even number (including zero) is reinforcing; an odd number is balancing.

Worked example, a restaurant with falling reviews:

```
R1 (decline spiral)
Staff workload -> (+) Staff turnover -> (+) Share of new staff
   -> (-) Service quality -> (+) Reviews -> (+) Customers
   -> (+) Revenue -> (+) Staffing budget -> (-) Staff workload

B1 (the owner's quick fix)
Falling revenue -> (+) Discounts -> (+) Customers (short term)
   but Discounts -> (+) Staff workload  || and  -> (-) Margin
```

Reading it: discounts bring customers back for a while (B1) but add workload and cut margin, which feeds the decline spiral (R1). The leverage is at staff turnover, not at price.

Keep maps small. Five to eight variables and two or three loops are enough; a map nobody can read helps nobody.

## 4. The eight archetypes

| Archetype | What it looks like | The trap | The way out |
|---|---|---|---|
| **Fixes that fail** | A quick fix works, then the problem returns worse. | The fix has a delayed side effect that feeds the problem. | Find the side effect; fix the cause, or pair the quick fix with a real one. |
| **Shifting the burden** | The business leans on a symptom-reliever (the owner stepping in, overtime, discounts) again and again. | Each use weakens the ability to solve it properly. | Build the real capability while reducing use of the crutch. |
| **Limits to growth** | Growth was strong, then slowed or stopped for no clear reason. | Pushing harder on what used to work. | Find the limiting factor (capacity, quality, management attention, cash) and relieve it. |
| **Growth and underinvestment** | Demand outruns capacity, quality drops, demand falls, so investment looks unnecessary. | Using falling demand as a reason not to invest. | Invest ahead of demand against a fixed standard. |
| **Drifting goals** | Targets are quietly lowered each time they are missed. | The lowered standard becomes normal. | Anchor the standard to something external (customer need, best competitor). |
| **Success to the successful** | One product, branch, or person gets more resources because they did well, and so does better still. | The other is starved, then judged as weak. | Check whether the early gap reflected real merit or just a head start. |
| **Escalation** | Two sides keep responding to each other (price wars, departmental one-upmanship). | Each move seems defensive and reasonable. | One side stops, or both agree a shared goal. |
| **Tragedy of the commons** | Everyone draws on a shared resource (a shared team, budget, brand, the owner's time) until it is exhausted. | Each user's draw is individually sensible. | Make the limit visible; ration or price the resource. |

If none fits, do not force one. Say the map stands on its own.

## 5. Leverage points

Places to intervene, from weakest to strongest. Most business fixes sit at the top of this list; the best ones sit lower.

1. **Numbers** - targets, budgets, prices, headcount. Easy to change, usually small effect.
2. **Buffers and capacity** - stock levels, cash reserves, spare time. They stabilise the system but do not redirect it.
3. **Delays** - shortening the time between action and feedback (weekly numbers where there were monthly ones).
4. **Information flows** - who sees what, and when. Showing a team its own results often changes behaviour without any new rule.
5. **Rules and incentives** - what is rewarded, punished, and allowed. People follow the incentive, not the mission statement.
6. **Who has the power to change the rules** - decision rights and structure.
7. **The goal of the system** - what it is actually optimising (for example, this month's sales versus customers who return).
8. **The beliefs behind the goal** - the assumptions leaders hold about customers, staff, and what the business is for.

When recommending a fix, say which level it sits at. If every proposal is at level 1, look deeper.

## 6. Starter breakdowns

Use these as first splits, then adapt to the business.

- **Revenue** = customers x purchases per customer x average order value. Customers = new + returning.
- **Profit** = revenue - variable costs - fixed costs. Check the margin per product and per customer, not just the total.
- **Cash** = cash in - cash out. Look at the timing: how long customers take to pay, how long stock sits, how soon suppliers must be paid. A profitable business can still run out of cash.
- **Customer loss** = customers who never return + customers who leave after a bad experience + customers taken by a competitor + customers whose need ended.
- **Staff turnover** = pay and fairness + the manager + workload + growth prospects + fit at hiring. Ask when people leave (month three and year three have different causes).
- **Slow operations** = find the bottleneck first. The slowest step sets the pace of the whole flow; speeding up any other step changes nothing.
- **Growth stall** = market limit, capacity limit, quality limit, or management attention limit. See "Limits to growth".
