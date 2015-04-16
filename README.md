# whose-turn
Randomly select an object by weighing the probability by some attribute. 
E.g. select who is going a present at the next group meeting, what movie to watch in next movie event.

Idea:
Let there be N objects
Select N numbers {p_i} using uniform distribution in [0,1). Let these numbers add up to M
Note that this number M, is uniformly distributed in [0,N).
Also, p_i is uniformly distributed in [0,M)
So without any weights, over a long period, all p_i should have the same probability of occuring.
Now, we should be able to affect these probabilities by weighing the probability of each one with a coefficient. Since all the numbers were randomly generated, the weighed probability should still be random (except it's no longer uniform).

\begin{equation}
\begin{split}
\sum_i p_i &= 1\\
\sum_i w_i p_i &= 1+\sum_j(w_j-1)p_j \mbox{ where $w_i>=0$}\\
\frac{\sum_i w_i p_i}{1+\sum_j(w_j-1)p_j} &= 1\\
\frac{\sum_i w_i p_i}{\sum_j w_j p_j} = &1\\
\end{split}
\end{equation}
Now if we wanted to increase/decrease the i'th probability by factor $k_i$, then 
\begin{equation}
\begin{split}
\frac{w_i}{\sum_j w_j p_j} &= k_i\\
w_i &= k_i \sum_j w_j p_j\\
0 &= (k_i p_i-1)w_i + \sum_{j\neq i}  k_i p_j w_j
\end{split}
\end{equation}
Note that this is a linear system, and if we wanted to find weights such that all the probability is change by a factor of $\vec{k}$, we create a linear system and solve for $\vec{w}$
Also note that I am lazy and have yet to implement this. Right now, we set the $\vec{w}$ directly instead of solving for it from $\vec{k}$.

But the general idea is that we can change the distribution, quite simply, by weighing them then renormalizing.

Group Meeting:
Each member is weighed by the number of weeks since their last presentation, where the weight is set to zero if number of weeks is less than 3.
The person with the largest number is selected to be the person to present on a given date.
The information on each presentation is stored by pickling the GroupMeetings instance in group_meeting.py of ./groupmeeting. 
We'd need to store and accesss this each time we assign. There's not that much information to store, so this shouldn't get too crazy heavy.
Github is used for transparency: if you think the weighing is unfair, feel free to modify, but we'd know exactly who modified it and how it was modified.




