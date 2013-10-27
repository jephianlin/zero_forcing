#This is a library of the 238 directed graphs on 1-4 vertices where they are ordered according to: R. C. Read and R. J. Wilson. An Atlas of Graphs. Oxford University Press, Oxford, 1998.

D = []
D.append('no graph')
D.append(DiGraph({0:[]}))#D1
D.append(DiGraph({0:[],1:[]}))#D2
D.append(DiGraph({0:[1]}))#D3
D.append(DiGraph({0:[1],1:[0]}))#D4
D.append(DiGraph({0:[],1:[],2:[]}))#D5
D.append(DiGraph({0:[],1:[2]}))#D6
D.append(DiGraph({0:[1,2],1:[],2:[]}))#D7
D.append(DiGraph({0:[],1:[2],2:[1]}))#D8
D.append(DiGraph({0:[2],1:[0],2:[]}))#D9
D.append(DiGraph({0:[],1:[0],2:[0]}))#D10
D.append(DiGraph({0:[],1:[0,2],2:[1]}))#D11
D.append(DiGraph({0:[2],1:[0,2],2:[]}))#D12
D.append(DiGraph({0:[1],1:[2],2:[1]}))#D13
D.append(DiGraph({0:[2],1:[0],2:[1]}))#D14
D.append(DiGraph({0:[],1:[0,2],2:[0,1]}))#D15
D.append(DiGraph({0:[1,2],1:[0],2:[0]}))#D16
D.append(DiGraph({0:[1,2],1:[2],2:[1]}))#D17
D.append(DiGraph({0:[2],1:[0,2],2:[1]}))#D18
D.append(DiGraph({0:[1,2],1:[0,2],2:[0]}))#D19
D.append(DiGraph({0:[1,2],1:[0,2],2:[0,1]}))#D20
D.append(DiGraph({0:[],1:[],2:[],3:[]}))#D21
D.append(DiGraph({0:[],1:[0],2:[],3:[]}))#D22
D.append(DiGraph({0:[],1:[2,3],2:[],3:[]}))#D23
D.append(DiGraph({0:[1],1:[0],2:[],3:[]}))#D24
D.append(DiGraph({0:[],1:[3],2:[1],3:[]}))#D25
D.append(DiGraph({0:[],1:[],2:[1],3:[1]}))#D26
D.append(DiGraph({0:[1],1:[],2:[3],3:[]}))#D27
D.append(DiGraph({0:[],1:[0,2,3],2:[],3:[]}))#D28
D.append(DiGraph({0:[],1:[2,3],2:[],3:[1]}))#D29
D.append(DiGraph({0:[],1:[2,3],2:[],3:[2]}))#D30
D.append(DiGraph({0:[],1:[0,2],2:[],3:[1]}))#D31
D.append(DiGraph({0:[1,2],1:[3],2:[],3:[]}))#D32
D.append(DiGraph({0:[1,2],1:[],2:[],3:[1]}))#D33
D.append(DiGraph({0:[],1:[3],2:[1],3:[1]}))#D34
D.append(DiGraph({0:[],1:[3],2:[1],3:[2]}))#D35
D.append(DiGraph({0:[],1:[0],2:[1],3:[1]}))#D36
D.append(DiGraph({0:[1],1:[0],2:[3],3:[]}))#D37
D.append(DiGraph({0:[1],1:[3],2:[0],3:[]}))#D38
D.append(DiGraph({0:[1],1:[],2:[0],3:[1]}))#D39
D.append(DiGraph({0:[1],1:[],2:[1],3:[1]}))#D40
D.append(DiGraph({0:[1],1:[0,2,3],2:[],3:[]}))#D41
D.append(DiGraph({0:[],1:[0,2,3],2:[],3:[2]}))#D42
D.append(DiGraph({0:[],1:[2,3],2:[],3:[1,2]}))#D43
D.append(DiGraph({0:[1,2],1:[0,3],2:[],3:[]}))#D44
D.append(DiGraph({0:[],1:[0,2],2:[],3:[1,2]}))#D45
D.append(DiGraph({0:[1,2],1:[],2:[],3:[1,2]}))#D46
D.append(DiGraph({0:[],1:[2,3],2:[1],3:[1]}))#D47
D.append(DiGraph({0:[],1:[3],2:[1,3],3:[2]}))#D48
D.append(DiGraph({0:[],1:[3],2:[1,3],3:[1]}))#D49
D.append(DiGraph({0:[1],1:[0,2],2:[],3:[1]}))#D50
D.append(DiGraph({0:[1,2],1:[0],2:[],3:[1]}))#D51
D.append(DiGraph({0:[1,2],1:[3],2:[0],3:[]}))#D52
D.append(DiGraph({0:[],1:[0,2],2:[3],3:[1]}))#D53
D.append(DiGraph({0:[2],1:[0,3],2:[0],3:[]}))#D54
D.append(DiGraph({0:[],1:[0],2:[1,3],3:[1]}))#D55
D.append(DiGraph({0:[1,2],1:[],2:[0],3:[1]}))#D56
D.append(DiGraph({0:[1],1:[2,3],2:[],3:[2]}))#D57
D.append(DiGraph({0:[1],1:[2],2:[],3:[1,2]}))#D58
D.append(DiGraph({0:[1,2],1:[3],2:[3],3:[]}))#D59
D.append(DiGraph({0:[1,2],1:[3],2:[],3:[2]}))#D60
D.append(DiGraph({0:[1],1:[],2:[1],3:[1,2]}))#D61
D.append(DiGraph({0:[1],1:[0],2:[1],3:[1]}))#D62
D.append(DiGraph({0:[1],1:[0],2:[0],3:[1]}))#D63
D.append(DiGraph({0:[2],1:[0],2:[0],3:[1]}))#D64
D.append(DiGraph({0:[1],1:[3],2:[1],3:[2]}))#D65
D.append(DiGraph({0:[1],1:[0],2:[3],3:[2]}))#D66
D.append(DiGraph({0:[1],1:[3],2:[0],3:[2]}))#D67
D.append(DiGraph({0:[],1:[0,2,3],2:[],3:[1,2]}))#D68
D.append(DiGraph({0:[1,2],1:[],2:[],3:[0,1,2]}))#D69
D.append(DiGraph({0:[1],1:[0,2,3],2:[1]}))#D70
D.append(DiGraph({0:[],1:[0,2,3],2:[3],3:[1]}))#D71
D.append(DiGraph({0:[],1:[0,2,3],2:[3],3:[2]}))#D72
D.append(DiGraph({0:[1],1:[0,2,3],2:[3]}))#D73
D.append(DiGraph({0:[1],2:[0,1,3],3:[0]}))#D74
D.append(DiGraph({0:[1,2,3],1:[2],3:[2]}))#D75
D.append(DiGraph({0:[],1:[2,3],2:[1],3:[1,2]}))#D76
D.append(DiGraph({0:[1],1:[0,2],2:[1,3]}))#D77
D.append(DiGraph({0:[],1:[0,3],2:[1],3:[1,2]}))#D78
D.append(DiGraph({0:[],1:[0,2],2:[1],3:[1,2]}))#D79
D.append(DiGraph({0:[],1:[0],2:[1,3],3:[1,2]}))#D80
D.append(DiGraph({0:[],1:[0,2],2:[3],3:[1,2]}))#D81
D.append(DiGraph({0:[1],1:[2,3],3:[1,2]}))#D82
D.append(DiGraph({0:[1],1:[0,2],3:[1,2]}))#D83
D.append(DiGraph({0:[],1:[0],2:[1,3],3:[0,2]}))#D84
D.append(DiGraph({0:[1,3],2:[0,1],3:[2]}))#D85
D.append(DiGraph({0:[1,3],2:[1,3],3:[2]}))#D86
D.append(DiGraph({0:[1],2:[0,1],3:[0,2]}))#D87
D.append(DiGraph({0:[1],2:[1,3],3:[1,2]}))#D88
D.append(DiGraph({0:[1,2],1:[2],3:[0,2]}))#D89
D.append(DiGraph({0:[2],1:[0,2],3:[0,2]}))#D90
D.append(DiGraph({0:[1],1:[0,2],2:[1],3:[1]}))#D91
D.append(DiGraph({0:[1],1:[0,2],2:[1],3:[2]}))#D92
D.append(DiGraph({0:[1],1:[2,3],2:[3],3:[1]}))#D93
D.append(DiGraph({0:[1],1:[3],2:[1],3:[1,2]}))#D94
D.append(DiGraph({0:[1],1:[3],2:[1,3],3:[2]}))#D95
D.append(DiGraph({0:[1],1:[2,3],2:[3],3:[2]}))#D96
D.append(DiGraph({0:[1],1:[3],2:[1,3],3:[1]}))#D97
D.append(DiGraph({0:[1],1:[0,2],2:[3],3:[1]}))#D98
D.append(DiGraph({0:[3],1:[0],2:[1],3:[0,2]}))#D99
D.append(DiGraph({0:[1],1:[0,2],2:[3],3:[2]}))#D100
D.append(DiGraph({0:[1,2],1:[2],2:[3],3:[0]}))#D101
D.append(DiGraph({0:[1,3],1:[2],2:[0],3:[2]}))#D102
D.append(DiGraph({0:[1],1:[0],2:[1,3],3:[1]}))#D103
D.append(DiGraph({0:[1,3],1:[2],2:[1],3:[2]}))#D104
D.append(DiGraph({0:[2],1:[0],2:[1],3:[0,2]}))#D105
D.append(DiGraph({0:[1,2,3],2:[0,1,3]}))#D106
D.append(DiGraph({0:[],1:[0,2,3],2:[1],3:[1,2]}))#D107
D.append(DiGraph({0:[],1:[0,2,3],2:[3],3:[1,2]}))#D108
D.append(DiGraph({0:[1],1:[0,2,3],2:[1,3]}))#D109
D.append(DiGraph({0:[1,2],2:[0,1,3],3:[0]}))#D110
D.append(DiGraph({0:[1,2,3],1:[0,2],2:[3]}))#D111
D.append(DiGraph({0:[1,2,3],1:[0],2:[1,3]}))#D112
D.append(DiGraph({0:[1,3],2:[0,1,3],3:[0]}))#D113
D.append(DiGraph({0:[1,2,3],1:[0,2],3:[2]}))#D114
D.append(DiGraph({0:[1,3],1:[3],2:[0,1,3]}))#D115 
D.append(DiGraph({0:[],1:[2,3],2:[1,3],3:[1,2]}))#D116
D.append(DiGraph({0:[],1:[0,2],2:[1,3],3:[1,2]}))#D117
D.append(DiGraph({0:[1,2],2:[0,1],3:[0,2]}))#D118
D.append(DiGraph({0:[1,3],1:[0,2],2:[0,3]}))#D119
D.append(DiGraph({0:[1,3],2:[1,3],3:[0,2]}))#D120
D.append(DiGraph({0:[1,2],1:[0,2],3:[0,2]}))#D121
D.append(DiGraph({0:[1,3],2:[0,1],3:[1,2]}))#D122
D.append(DiGraph({0:[1,2,3],1:[0],2:[0],3:[0]}))#D123
D.append(DiGraph({0:[1,2,3],1:[0],2:[0],3:[2]}))#D124
D.append(DiGraph({0:[2],1:[0],2:[0,1,3],3:[0]}))#D125
D.append(DiGraph({0:[1,2,3],1:[0],2:[1],3:[2]}))#D126
D.append(DiGraph({0:[1,2,3],1:[0],2:[3],3:[2]}))#D127
D.append(DiGraph({0:[1],1:[0],2:[0,1,3],3:[0]}))#D128
D.append(DiGraph({0:[1,2,3],1:[2],2:[3],3:[1]}))#D129
D.append(DiGraph({0:[2,3],1:[0],2:[0],3:[0,2]}))#D130
D.append(DiGraph({0:[1],1:[2,3],2:[3],3:[1,2]}))#D131
D.append(DiGraph({0:[1],1:[3],2:[1,3],3:[1,2]}))#D132
D.append(DiGraph({0:[1],1:[0,2],2:[1,3],3:[1]}))#D133
D.append(DiGraph({0:[1],1:[0,2],2:[1,3],3:[2]}))#D134
D.append(DiGraph({0:[2,3],1:[0],2:[0,1],3:[2]}))#D135
D.append(DiGraph({0:[1],1:[0,2],2:[1],3:[1,2]}))#D136
D.append(DiGraph({0:[1,3],1:[2],2:[3],3:[0,2]}))#D137
D.append(DiGraph({0:[1,2],1:[0,2],2:[3],3:[0]}))#D138
D.append(DiGraph({0:[1,3],1:[0,2],2:[0],3:[2]}))#D139
D.append(DiGraph({0:[1],1:[0,2],2:[3],3:[1,2]}))#D140
D.append(DiGraph({0:[1,3],1:[2],2:[0,3],3:[0]}))#D141
D.append(DiGraph({0:[1,2],1:[0],2:[1,3],3:[0]}))#D142
D.append(DiGraph({0:[2],1:[0],2:[0,1],3:[0,2]}))#D143
D.append(DiGraph({0:[1],1:[0],2:[1,3],3:[1,2]}))#D144
D.append(DiGraph({0:[1],1:[0,2],2:[0,3],3:[0]}))#D145
D.append(DiGraph({0:[3],1:[0,2],2:[3],3:[0,2]}))#D146
D.append(DiGraph({0:[1,2],1:[0],2:[1],3:[0,2]}))#D147
D.append(DiGraph({0:[3],1:[0,2],2:[1,3],3:[0]}))#D148
D.append(DiGraph({0:[2,3],1:[0,2],2:[3],3:[1]}))#D149
D.append(DiGraph({0:[3],1:[0,2],2:[1],3:[0,2]}))#D150
D.append(DiGraph({0:[1],1:[0,2],2:[0],3:[0,2]}))#D151
D.append(DiGraph({0:[1],1:[0],2:[0,1],3:[0,2]}))#D152
D.append(DiGraph({0:[2],1:[0,2],2:[0],3:[0,2]}))#D153
D.append(DiGraph({0:[1,2,3],1:[3],2:[],3:[1,0,2]}))#D154
D.append(DiGraph({0:[1,2,3],1:[0,2,3],2:[3],3:[]}))#D155
D.append(DiGraph({0:[],1:[0,2,3],2:[1,3],3:[1,2]}))#D156
D.append(DiGraph({0:[1,2,3],1:[0,3],2:[],3:[0,2]}))#D157
D.append(DiGraph({0:[1,2,3],1:[0,3],2:[],3:[1,2]}))#D158
D.append(DiGraph({0:[1,2,3],1:[0,3],2:[0,3],3:[]}))#D159
D.append(DiGraph({0:[1,2],1:[0,2,3],2:[],3:[2,0]}))#D160
D.append(DiGraph({0:[1,2],1:[0,2],2:[],3:[0,1,2]}))#D161
D.append(DiGraph({0:[1],1:[0,2,3],2:[1],3:[1,2]}))#D162
D.append(DiGraph({0:[1,3],1:[3],2:[0],3:[0,1,2]}))#D163
D.append(DiGraph({0:[1],1:[0,2,3],2:[3],3:[1,2]}))#D164
D.append(DiGraph({0:[1,2,3],1:[3],2:[3],3:[0,1]}))#D165
D.append(DiGraph({0:[1,2,3],1:[0,3],2:[3],3:[0]}))#D166
D.append(DiGraph({0:[1,2,3],1:[0,3],2:[3],3:[1]}))#D167
D.append(DiGraph({0:[1,2,3],1:[0],2:[0,3],3:[1]}))#D168
D.append(DiGraph({0:[1,2,3],1:[0],2:[0],3:[1,2]}))#D169
D.append(DiGraph({0:[1,2],1:[0,2,3],2:[3],3:[0]}))#D170
D.append(DiGraph({0:[1,2,3],1:[0],2:[3],3:[1,2]}))#D171
D.append(DiGraph({0:[1,2],1:[0],2:[0],3:[0,1,2]}))#D172
D.append(DiGraph({0:[1,2,3],1:[0,3],2:[3],3:[2]}))#D173
D.append(DiGraph({0:[1],1:[0,2,3],2:[0,3],3:[0]}))#D174
D.append(DiGraph({0:[1],1:[0,2],2:[0],3:[0,1,2]}))#D175
D.append(DiGraph({0:[1],1:[0],2:[0,1,3],3:[0,1]}))#D176
D.append(DiGraph({0:[1],1:[2,3],2:[1,3],3:[1,2]}))#D177
D.append(DiGraph({0:[1,3],1:[0,3],2:[0],3:[2,0]}))#D178
D.append(DiGraph({0:[1],1:[0,3],2:[1,3],3:[1,2]}))#D179
D.append(DiGraph({0:[1,3],1:[0,3],2:[0],3:[1,2]}))#D180
D.append(DiGraph({0:[1,3],1:[3],2:[0,3],3:[0,1]}))#D181
D.append(DiGraph({0:[1,2],1:[0,3],2:[0,3],3:[0]}))#D182
D.append(DiGraph({0:[1,2],1:[0],2:[0,3],3:[0,1]}))#D183
D.append(DiGraph({0:[2],1:[0,3],2:[0,3],3:[1,2]}))#D184
D.append(DiGraph({0:[1,2],1:[0,2],2:[3],3:[0,1]}))#D185
D.append(DiGraph({0:[1,3],1:[0,2],2:[0,3],3:[1]}))#D186
D.append(DiGraph({0:[1,3],1:[0],2:[0,3],3:[1,2]}))#D187
D.append(DiGraph({0:[1,3],1:[0,3],2:[0,3],3:[0]}))#D188
D.append(DiGraph({0:[1,3],1:[0,3],2:[0,3],3:[1]}))#D189
D.append(DiGraph({0:[1,3],1:[0,3],2:[0,3],3:[2]}))#D190
D.append(DiGraph({0:[1],1:[0,2],2:[0,3],3:[0,1]}))#D191
D.append(DiGraph({0:[1,2,3],1:[0,2],2:[0,1,3]}))#D192
D.append(DiGraph({0:[1,2,3],1:[0,2,3],2:[1,3]}))#D193
D.append(DiGraph({0:[1,2,3],1:[2],2:[0,1,3],3:[2]}))#D194
D.append(DiGraph({0:[1,2,3],1:[2],2:[0,1,3],3:[0]}))#D195
D.append(DiGraph({0:[1,2,3],1:[0,2,3],2:[1],3:[2]}))#D196
D.append(DiGraph({0:[1,2,3],1:[0,2,3],2:[3],3:[2]}))#D197
D.append(DiGraph({0:[1],1:[0,2,3],2:[1,3],3:[1,2]}))#D198
D.append(DiGraph({0:[1,2],1:[0,2],2:[0,1,3],3:[0]}))#D199
D.append(DiGraph({0:[1,2],1:[2],2:[0,1,3],3:[0,2]}))#D200
D.append(DiGraph({0:[1,2,3],1:[0,2],2:[0,3],3:[2]}))#D201
D.append(DiGraph({0:[1,2],1:[0,2,3],2:[1,3],3:[0]}))#D202
D.append(DiGraph({0:[1,2,3],1:[0,2],2:[1,3],3:[0]}))#D203
D.append(DiGraph({0:[1,2,3],1:[0,2],2:[1,3],3:[1]}))#D204
D.append(DiGraph({0:[1,2,3],1:[0,2],2:[1,3],3:[2]}))#D205
D.append(DiGraph({0:[1,2,3],1:[0,2],2:[0],3:[0,2]}))#D206
D.append(DiGraph({0:[1,2],1:[0,2,3],2:[1],3:[0,2]}))#D207
D.append(DiGraph({0:[1,2,3],1:[0,2],2:[1],3:[0,2]}))#D208
D.append(DiGraph({0:[1,2,3],1:[0,2],2:[1],3:[1,2]}))#D209
D.append(DiGraph({0:[1,2],1:[0,2,3],2:[3],3:[0,2]}))#D210
D.append(DiGraph({0:[1,2],1:[0,2],2:[3],3:[0,1,2]}))#D211
D.append(DiGraph({0:[1,2],1:[0,2],2:[1],3:[0,1,2]}))#D212
D.append(DiGraph({0:[1,2],1:[0,2],2:[0,1],3:[0,2]}))#D213
D.append(DiGraph({0:[1,2],1:[0,2],2:[0,3],3:[0,2]}))#D214
D.append(DiGraph({0:[1,2],1:[0,2],2:[1,3],3:[0,1]}))#D215
D.append(DiGraph({0:[1,2],1:[0,2],2:[1,3],3:[0,2]}))#D216
D.append(DiGraph({0:[1,3],1:[0,2],2:[1,3],3:[0,2]}))#D217
D.append(DiGraph({0:[1,3],1:[0,2],2:[0,3],3:[1,2]}))#D218
D.append(DiGraph({0:[1,2,3],1:[0,2,3],2:[0,1,3]}))#D219
D.append(DiGraph({0:[1,2,3],1:[0,2],2:[0,1,3],3:[2]}))#D220
D.append(DiGraph({0:[1,2,3],1:[0,2,3],2:[0,1],3:[2]}))#D221
D.append(DiGraph({0:[1,2,3],1:[0,2,3],2:[1,3],3:[1]}))#D222
D.append(DiGraph({0:[1,2,3],1:[0,2,3],2:[1,3],3:[0]}))#D223
D.append(DiGraph({0:[1,2,3],1:[0,2,3],2:[1,3],3:[2]}))#D224
D.append(DiGraph({0:[1,2],1:[0,2],2:[0,1,3],3:[0,2]}))#D225
D.append(DiGraph({0:[1,2],1:[0,2,3],2:[0,1],3:[0,2]}))#D226
D.append(DiGraph({0:[1,2],1:[0,2,3],2:[1,3],3:[0,1]}))#D227
D.append(DiGraph({0:[1,2],1:[0,2,3],2:[1,3],3:[0,2]}))#D228
D.append(DiGraph({0:[1,2,3],1:[0,2],2:[1,3],3:[0,2]}))#D229
D.append(DiGraph({0:[1,2,3],1:[0,2],2:[1,3],3:[1,2]}))#D230
D.append(DiGraph({0:[1,2],1:[0,2],2:[0,1],3:[0,1,2]}))#D231
D.append(DiGraph({0:[1,2,3],1:[0,2,3],2:[0,1,3],3:[1]}))#D232
D.append(DiGraph({0:[1,2,3],1:[0,2],2:[0,1,3],3:[0,2]}))#D233
D.append(DiGraph({0:[1,2,3],1:[0,2,3],2:[0,1],3:[1,2]}))#D234
D.append(DiGraph({0:[1,2],1:[0,2,3],2:[0,1],3:[0,1,2]}))#D235
D.append(DiGraph({0:[2,3],1:[0,2,3],2:[0,1],3:[0,1,2]}))#D236
D.append(DiGraph({0:[1,2,3],1:[0,2,3],2:[0,1],3:[0,1,2]}))#D237
D.append(DiGraph({0:[1,2,3],1:[0,2,3],2:[0,1,3],3:[0,1,2]}))#D238

directed_atlas = []
i=0
while i <=238:
    directed_atlas.append(D[i])
    i+=1