import matplotlib.pyplot as plt
import math
import numpy as np
import plotly.express as px
plt.style.use('ggplot')


N = np.arange(1.1, 10, 0.01)

fns = {
    'N': lambda N: N,
    'log(N)': lambda N: math.log(N),
    'log(log(N))': lambda N: math.log(math.log(N)),
    'sqrt(N)': lambda N: math.sqrt(N),
    'Nlog(N)': lambda N: N*math.log(N),
    'Nlog(log(N))': lambda N: N*math.log(math.log(N)),
    'Nsqrt(N)': lambda N: N*math.sqrt(N),
    # 'N^2': lambda N: N**2,
    # '2^N': lambda N: 2**N,
    # 'N!': lambda N: math.factorial(N),
}

# plt.figure(figsize=(10, 7))
# plt.title('Complexities')
# for fn in fns:
#     plt.plot(N, [fns[fn](n) for n in N], label=fn)
#     plt.xlabel(fn)
#     plt.ylabel('Time')
#     plt.legend()
# plt.show()


for fn in fns:
    points = [fns[fn](n) for n in N]
    fig = px.line(x=N, y=[fns[fn](n) for n in N], color=points,
                  line_group=points, hover_name=points)
fig.show(renderer='png')
