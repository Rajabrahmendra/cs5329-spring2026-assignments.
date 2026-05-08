# Analysis

# Analysis

## Greedy strategy 1

Greedy1 sorts tasks by the earliest finish time and picks each one only if it fits into the schedule. The logic is simple: when you finish a task sooner, you leave yourself more options for what comes next.

I figured Greedy1 would work especially well when tasks aren’t crammed together, when getting things done early means more freedom later. And honestly, sometimes it nailed it. In sparse schedules, Greedy1 matched brute force exactly. Even on some bigger benchmarks, it actually outperformed Greedy2 by grabbing a higher total weight.

But Greedy1 definitely has some blind spots. It focuses so much on finishing early that it sometimes misses better options—combinations that could give you a bigger total value. Just because something ends quickly doesn’t make it the best pick. The `simple.json` test made that obvious: brute force found a total weight of 83.0, while Greedy1 only got 79.5. The adversarial test was even rougher, with brute force hitting 100 as Greedy1 trailed far behind at 25. So, Greedy1 is fast and often good enough, but it doesn’t always find the best answer.


## Greedy strategy 2

Greedy2 sorts the tasks by weight per resource. It then checks each task one by one and adds a task only if the schedule remains valid. The goal is to prefer tasks that provide more value for each unit of resource used. This approach can be useful when resource capacity is limited.

I expected Greedy2 to perform well when resource usage was the main challenge. In some tests, it exceeded expectations. In `sample2.json`, Greedy2 outperformed Greedy1. In the adversarial case, Greedy2 matched brute force with a total weight of 100.

However, Greedy2 is not always the best option. It emphasizes local efficiency rather than the entire schedule. A task may seem favorable because its weight-to-resource ratio is high, but that task might prevent a better overall combination later. This occurred in `simple.json`, where brute force scored 83.0, while Greedy2 only achieved 73.5. Additionally, it provided a lower total weight than Greedy1 in larger benchmark tests. So, while Greedy2 is quick and performs well at times, it does not guarantee the optimal solution.

## Small test case validation

I used brute force on five small test cases and compared the greedy methods with the optimal result.


| Case        | Brute | Greedy1 | Greedy2 |
|-------------|------:|--------:|--------:|
| simple      |  83.0 |    79.5 |    73.5 |
| sparse      | 360.45|   360.45|   360.45|
| adversarial | 100.0 |    25.0 |   100.0 |
| sample2     |  95.0 |    88.0 |    91.0 |
| sample3     |  60.0 |    53.0 |    52.0 |

The results reveal that neither greedy approach consistently emerges as the top choice. In situations with sparse data, both greedy methods equaled brute force. However, when facing adversarial conditions, while greedy2 aligned with brute force, greedy1 performed poorly. In simpler scenarios, brute force outshined both greedy methods, with greedy2 falling short even more. Looking at `sample2.json`, greedy2 surpassed greedy1. Meanwhile, in `sample3.json`, greedy1 had a slight edge over greedy2. 

Thus, these smaller test cases highlight a pattern: both greedy strategies can succeed in certain situations but are also prone to failure in others.

## Benchmark comparison

I also tested the greedy methods on larger inputs.

| Size | Greedy1 Weight | Greedy1 Time | Greedy2 Weight | Greedy2 Time |
|------|---------------:|-------------:|---------------:|-------------:|
| 100  | 2430.75        | 0.002406     | 2349.31        | 0.002512     |
| 500  | 5129.74        | 0.044224     | 4432.85        | 0.028377     |
| 1000 | 8649.20        | 0.223662     | 7273.45        | 0.151787     |


## Benchmark analysis

Greedy1 came out on top for total weight overall. In all the bigger benchmark tests, greedy1 pulled ahead—especially at 500 and 1000 tasks. The difference at 100 tasks was barely noticeable, but once the task load increased, greedy1’s advantage really showed. It just handled the tougher scheduling decisions better.

Greedy2, on the other hand, was quicker with the large inputs. At both 500 and 1000 tasks, it finished faster than greedy1. So there’s a real tradeoff here: greedy1 made more effective schedules, but greedy2 saved time.

Both strategies had weak spots. Greedy1 really struggled with the adversarial test, coming up with just 25, while brute force managed 100. That’s a good reminder—picking the earliest finish time can sometimes go completely wrong. Greedy2 had a hard time in the simple test. Brute force got 83.0, but greedy2 got stuck at 73.5. So picking by weight per resource can also miss some great combinations.

The category constraint made everything harder for both. Sometimes a task seemed perfect—either it finished early or had a great ratio—but if the schedule had too many overlapping tasks from the same category, it cut off future possibilities. That rule made it tough to count on the greedy strategies the way you might in a more basic scheduling problem.


## Reflection

This problem cannot be solved optimally by a simple greedy strategy in general. The reason is that each choice affects later choices in several ways at the same time. A task changes time overlap, resource use, and category overlap together. Because of that, a choice that looks good at one step may not lead to the best final answer.

For a greedy method to always work, the problem would need a stronger property where the best local choice is always part of the best overall solution. This problem does not have that property. My test results showed that clearly, because both greedy methods failed in some cases.

If I had to solve this in a real system, I would not depend only on greedy. I would use a greedy method as a fast starting point, but then improve the result with a better search method, such as branch and bound or integer programming. That would give better final schedules when accuracy matters more.