from Classes_ import State

d3 = State('d3')
d2 = State('d2')
d1 = State('d1')
c3 = State('c3')
c2 = State('c2')
c1 = State('c1')
b1 = State('b1')
a10 = State('a10')
a9 = State('a9')
a8 = State('a8')
a7 = State('a7')
a6 = State('a6')
a5 = State('a5')
a4 = State('a4')
a3 = State('a3')
a2 = State('a2')
a1 = State('a1')
a0 = State('a0')
a0.add_transition(123, a1)
a0.add_transition(97, b1)
a0.add_transition(98, b1)
a0.add_transition(99, b1)
a0.add_transition(100, b1)
a0.add_transition(101, b1)
a0.add_transition(102, b1)
a0.add_transition(103, b1)
a0.add_transition(104, b1)
a0.add_transition(105, b1)
a0.add_transition(106, b1)
a0.add_transition(107, b1)
a0.add_transition(108, b1)
a0.add_transition(109, b1)
a0.add_transition(110, b1)
a0.add_transition(111, b1)
a0.add_transition(112, b1)
a0.add_transition(113, b1)
a0.add_transition(114, b1)
a0.add_transition(115, b1)
a0.add_transition(116, b1)
a0.add_transition(117, b1)
a0.add_transition(118, b1)
a0.add_transition(119, b1)
a0.add_transition(120, b1)
a0.add_transition(121, b1)
a0.add_transition(122, b1)
a0.add_transition(39, c1)
a0.add_transition(34, d1)

a1.add_transition(32, a1)
a1.add_transition(114, a2)

a2.add_transition(101, a3)

a3.add_transition(116, a4)

a4.add_transition(117, a5)

a5.add_transition(114, a6)

a6.add_transition(110, a7)

a7.add_transition(32, a7)
a7.add_transition(65, a8)
a7.add_transition(66, a8)
a7.add_transition(67, a8)
a7.add_transition(68, a8)
a7.add_transition(69, a8)
a7.add_transition(70, a8)
a7.add_transition(71, a8)
a7.add_transition(72, a8)
a7.add_transition(73, a8)
a7.add_transition(74, a8)
a7.add_transition(75, a8)
a7.add_transition(76, a8)
a7.add_transition(77, a8)
a7.add_transition(78, a8)
a7.add_transition(79, a8)
a7.add_transition(80, a8)
a7.add_transition(81, a8)
a7.add_transition(82, a8)
a7.add_transition(83, a8)
a7.add_transition(84, a8)
a7.add_transition(85, a8)
a7.add_transition(86, a8)
a7.add_transition(87, a8)
a7.add_transition(88, a8)
a7.add_transition(89, a8)
a7.add_transition(90, a8)

a8.add_transition(32, a9)
a8.add_transition(65, a8)
a8.add_transition(66, a8)
a8.add_transition(67, a8)
a8.add_transition(68, a8)
a8.add_transition(69, a8)
a8.add_transition(70, a8)
a8.add_transition(71, a8)
a8.add_transition(72, a8)
a8.add_transition(73, a8)
a8.add_transition(74, a8)
a8.add_transition(75, a8)
a8.add_transition(76, a8)
a8.add_transition(77, a8)
a8.add_transition(78, a8)
a8.add_transition(79, a8)
a8.add_transition(80, a8)
a8.add_transition(81, a8)
a8.add_transition(82, a8)
a8.add_transition(83, a8)
a8.add_transition(84, a8)
a8.add_transition(85, a8)
a8.add_transition(86, a8)
a8.add_transition(87, a8)
a8.add_transition(88, a8)
a8.add_transition(89, a8)
a8.add_transition(90, a8)
a8.add_transition(125, a10)

a9.add_transition(32, a9)
a9.add_transition(125, a10)

a10.isFinalState = True
a10.addToken( 'RETURN')

b1.isFinalState = True
b1.addToken( 'TOKEN')
b1.add_transition(97, b1)
b1.add_transition(98, b1)
b1.add_transition(99, b1)
b1.add_transition(100, b1)
b1.add_transition(101, b1)
b1.add_transition(102, b1)
b1.add_transition(103, b1)
b1.add_transition(104, b1)
b1.add_transition(105, b1)
b1.add_transition(106, b1)
b1.add_transition(107, b1)
b1.add_transition(108, b1)
b1.add_transition(109, b1)
b1.add_transition(110, b1)
b1.add_transition(111, b1)
b1.add_transition(112, b1)
b1.add_transition(113, b1)
b1.add_transition(114, b1)
b1.add_transition(115, b1)
b1.add_transition(116, b1)
b1.add_transition(117, b1)
b1.add_transition(118, b1)
b1.add_transition(119, b1)
b1.add_transition(120, b1)
b1.add_transition(121, b1)
b1.add_transition(122, b1)

c1.add_transition(9, c2)
c1.add_transition(10, c2)
c1.add_transition(13, c2)
c1.add_transition(33, c2)
c1.add_transition(34, c2)
c1.add_transition(35, c2)
c1.add_transition(36, c2)
c1.add_transition(37, c2)
c1.add_transition(38, c2)
c1.add_transition(39, c2)
c1.add_transition(40, c2)
c1.add_transition(41, c2)
c1.add_transition(42, c2)
c1.add_transition(43, c2)
c1.add_transition(44, c2)
c1.add_transition(45, c2)
c1.add_transition(46, c2)
c1.add_transition(47, c2)
c1.add_transition(48, c2)
c1.add_transition(49, c2)
c1.add_transition(50, c2)
c1.add_transition(51, c2)
c1.add_transition(52, c2)
c1.add_transition(53, c2)
c1.add_transition(54, c2)
c1.add_transition(55, c2)
c1.add_transition(56, c2)
c1.add_transition(57, c2)
c1.add_transition(58, c2)
c1.add_transition(59, c2)
c1.add_transition(60, c2)
c1.add_transition(61, c2)
c1.add_transition(62, c2)
c1.add_transition(63, c2)
c1.add_transition(64, c2)
c1.add_transition(65, c2)
c1.add_transition(66, c2)
c1.add_transition(67, c2)
c1.add_transition(68, c2)
c1.add_transition(69, c2)
c1.add_transition(70, c2)
c1.add_transition(71, c2)
c1.add_transition(72, c2)
c1.add_transition(73, c2)
c1.add_transition(74, c2)
c1.add_transition(75, c2)
c1.add_transition(76, c2)
c1.add_transition(77, c2)
c1.add_transition(78, c2)
c1.add_transition(79, c2)
c1.add_transition(80, c2)
c1.add_transition(81, c2)
c1.add_transition(82, c2)
c1.add_transition(83, c2)
c1.add_transition(84, c2)
c1.add_transition(85, c2)
c1.add_transition(86, c2)
c1.add_transition(87, c2)
c1.add_transition(88, c2)
c1.add_transition(89, c2)
c1.add_transition(90, c2)
c1.add_transition(91, c2)
c1.add_transition(92, c2)
c1.add_transition(93, c2)
c1.add_transition(94, c2)
c1.add_transition(95, c2)
c1.add_transition(96, c2)
c1.add_transition(97, c2)
c1.add_transition(98, c2)
c1.add_transition(99, c2)
c1.add_transition(100, c2)
c1.add_transition(101, c2)
c1.add_transition(102, c2)
c1.add_transition(103, c2)
c1.add_transition(104, c2)
c1.add_transition(105, c2)
c1.add_transition(106, c2)
c1.add_transition(107, c2)
c1.add_transition(108, c2)
c1.add_transition(109, c2)
c1.add_transition(110, c2)
c1.add_transition(111, c2)
c1.add_transition(112, c2)
c1.add_transition(113, c2)
c1.add_transition(114, c2)
c1.add_transition(115, c2)
c1.add_transition(116, c2)
c1.add_transition(117, c2)
c1.add_transition(118, c2)
c1.add_transition(119, c2)
c1.add_transition(120, c2)
c1.add_transition(121, c2)
c1.add_transition(122, c2)
c1.add_transition(123, c2)
c1.add_transition(124, c2)
c1.add_transition(125, c2)
c1.add_transition(126, c2)
c1.add_transition(192, c2)
c1.add_transition(193, c2)
c1.add_transition(194, c2)
c1.add_transition(195, c2)
c1.add_transition(196, c2)
c1.add_transition(197, c2)
c1.add_transition(198, c2)
c1.add_transition(199, c2)
c1.add_transition(200, c2)
c1.add_transition(201, c2)
c1.add_transition(202, c2)
c1.add_transition(203, c2)
c1.add_transition(204, c2)
c1.add_transition(205, c2)
c1.add_transition(206, c2)
c1.add_transition(207, c2)
c1.add_transition(208, c2)
c1.add_transition(209, c2)
c1.add_transition(210, c2)
c1.add_transition(211, c2)
c1.add_transition(212, c2)
c1.add_transition(213, c2)
c1.add_transition(214, c2)
c1.add_transition(215, c2)
c1.add_transition(216, c2)
c1.add_transition(217, c2)
c1.add_transition(218, c2)
c1.add_transition(219, c2)
c1.add_transition(220, c2)
c1.add_transition(221, c2)
c1.add_transition(222, c2)
c1.add_transition(223, c2)
c1.add_transition(224, c2)
c1.add_transition(225, c2)
c1.add_transition(226, c2)
c1.add_transition(227, c2)
c1.add_transition(228, c2)
c1.add_transition(229, c2)
c1.add_transition(230, c2)
c1.add_transition(231, c2)
c1.add_transition(232, c2)
c1.add_transition(233, c2)
c1.add_transition(234, c2)
c1.add_transition(235, c2)
c1.add_transition(236, c2)
c1.add_transition(237, c2)
c1.add_transition(238, c2)
c1.add_transition(239, c2)
c1.add_transition(240, c2)
c1.add_transition(241, c2)
c1.add_transition(242, c2)
c1.add_transition(243, c2)
c1.add_transition(244, c2)
c1.add_transition(245, c2)
c1.add_transition(246, c2)
c1.add_transition(247, c2)
c1.add_transition(248, c2)
c1.add_transition(249, c2)
c1.add_transition(250, c2)
c1.add_transition(251, c2)
c1.add_transition(252, c2)
c1.add_transition(253, c2)
c1.add_transition(254, c2)

c2.add_transition(39, c3)

c3.isFinalState = True
c3.addToken( 'SYMBOL')

d1.add_transition(9, d2)
d1.add_transition(10, d2)
d1.add_transition(13, d2)
d1.add_transition(33, d2)
d1.add_transition(34, d2)
d1.add_transition(35, d2)
d1.add_transition(36, d2)
d1.add_transition(37, d2)
d1.add_transition(38, d2)
d1.add_transition(39, d2)
d1.add_transition(40, d2)
d1.add_transition(41, d2)
d1.add_transition(42, d2)
d1.add_transition(43, d2)
d1.add_transition(44, d2)
d1.add_transition(45, d2)
d1.add_transition(46, d2)
d1.add_transition(47, d2)
d1.add_transition(48, d2)
d1.add_transition(49, d2)
d1.add_transition(50, d2)
d1.add_transition(51, d2)
d1.add_transition(52, d2)
d1.add_transition(53, d2)
d1.add_transition(54, d2)
d1.add_transition(55, d2)
d1.add_transition(56, d2)
d1.add_transition(57, d2)
d1.add_transition(58, d2)
d1.add_transition(59, d2)
d1.add_transition(60, d2)
d1.add_transition(61, d2)
d1.add_transition(62, d2)
d1.add_transition(63, d2)
d1.add_transition(64, d2)
d1.add_transition(65, d2)
d1.add_transition(66, d2)
d1.add_transition(67, d2)
d1.add_transition(68, d2)
d1.add_transition(69, d2)
d1.add_transition(70, d2)
d1.add_transition(71, d2)
d1.add_transition(72, d2)
d1.add_transition(73, d2)
d1.add_transition(74, d2)
d1.add_transition(75, d2)
d1.add_transition(76, d2)
d1.add_transition(77, d2)
d1.add_transition(78, d2)
d1.add_transition(79, d2)
d1.add_transition(80, d2)
d1.add_transition(81, d2)
d1.add_transition(82, d2)
d1.add_transition(83, d2)
d1.add_transition(84, d2)
d1.add_transition(85, d2)
d1.add_transition(86, d2)
d1.add_transition(87, d2)
d1.add_transition(88, d2)
d1.add_transition(89, d2)
d1.add_transition(90, d2)
d1.add_transition(91, d2)
d1.add_transition(92, d2)
d1.add_transition(93, d2)
d1.add_transition(94, d2)
d1.add_transition(95, d2)
d1.add_transition(96, d2)
d1.add_transition(97, d2)
d1.add_transition(98, d2)
d1.add_transition(99, d2)
d1.add_transition(100, d2)
d1.add_transition(101, d2)
d1.add_transition(102, d2)
d1.add_transition(103, d2)
d1.add_transition(104, d2)
d1.add_transition(105, d2)
d1.add_transition(106, d2)
d1.add_transition(107, d2)
d1.add_transition(108, d2)
d1.add_transition(109, d2)
d1.add_transition(110, d2)
d1.add_transition(111, d2)
d1.add_transition(112, d2)
d1.add_transition(113, d2)
d1.add_transition(114, d2)
d1.add_transition(115, d2)
d1.add_transition(116, d2)
d1.add_transition(117, d2)
d1.add_transition(118, d2)
d1.add_transition(119, d2)
d1.add_transition(120, d2)
d1.add_transition(121, d2)
d1.add_transition(122, d2)
d1.add_transition(123, d2)
d1.add_transition(124, d2)
d1.add_transition(125, d2)
d1.add_transition(126, d2)
d1.add_transition(192, d2)
d1.add_transition(193, d2)
d1.add_transition(194, d2)
d1.add_transition(195, d2)
d1.add_transition(196, d2)
d1.add_transition(197, d2)
d1.add_transition(198, d2)
d1.add_transition(199, d2)
d1.add_transition(200, d2)
d1.add_transition(201, d2)
d1.add_transition(202, d2)
d1.add_transition(203, d2)
d1.add_transition(204, d2)
d1.add_transition(205, d2)
d1.add_transition(206, d2)
d1.add_transition(207, d2)
d1.add_transition(208, d2)
d1.add_transition(209, d2)
d1.add_transition(210, d2)
d1.add_transition(211, d2)
d1.add_transition(212, d2)
d1.add_transition(213, d2)
d1.add_transition(214, d2)
d1.add_transition(215, d2)
d1.add_transition(216, d2)
d1.add_transition(217, d2)
d1.add_transition(218, d2)
d1.add_transition(219, d2)
d1.add_transition(220, d2)
d1.add_transition(221, d2)
d1.add_transition(222, d2)
d1.add_transition(223, d2)
d1.add_transition(224, d2)
d1.add_transition(225, d2)
d1.add_transition(226, d2)
d1.add_transition(227, d2)
d1.add_transition(228, d2)
d1.add_transition(229, d2)
d1.add_transition(230, d2)
d1.add_transition(231, d2)
d1.add_transition(232, d2)
d1.add_transition(233, d2)
d1.add_transition(234, d2)
d1.add_transition(235, d2)
d1.add_transition(236, d2)
d1.add_transition(237, d2)
d1.add_transition(238, d2)
d1.add_transition(239, d2)
d1.add_transition(240, d2)
d1.add_transition(241, d2)
d1.add_transition(242, d2)
d1.add_transition(243, d2)
d1.add_transition(244, d2)
d1.add_transition(245, d2)
d1.add_transition(246, d2)
d1.add_transition(247, d2)
d1.add_transition(248, d2)
d1.add_transition(249, d2)
d1.add_transition(250, d2)
d1.add_transition(251, d2)
d1.add_transition(252, d2)
d1.add_transition(253, d2)
d1.add_transition(254, d2)

d2.add_transition(9, d2)
d2.add_transition(10, d2)
d2.add_transition(13, d2)
d2.add_transition(33, d2)
d2.add_transition(34, d3)
d2.add_transition(35, d2)
d2.add_transition(36, d2)
d2.add_transition(37, d2)
d2.add_transition(38, d2)
d2.add_transition(39, d2)
d2.add_transition(40, d2)
d2.add_transition(41, d2)
d2.add_transition(42, d2)
d2.add_transition(43, d2)
d2.add_transition(44, d2)
d2.add_transition(45, d2)
d2.add_transition(46, d2)
d2.add_transition(47, d2)
d2.add_transition(48, d2)
d2.add_transition(49, d2)
d2.add_transition(50, d2)
d2.add_transition(51, d2)
d2.add_transition(52, d2)
d2.add_transition(53, d2)
d2.add_transition(54, d2)
d2.add_transition(55, d2)
d2.add_transition(56, d2)
d2.add_transition(57, d2)
d2.add_transition(58, d2)
d2.add_transition(59, d2)
d2.add_transition(60, d2)
d2.add_transition(61, d2)
d2.add_transition(62, d2)
d2.add_transition(63, d2)
d2.add_transition(64, d2)
d2.add_transition(65, d2)
d2.add_transition(66, d2)
d2.add_transition(67, d2)
d2.add_transition(68, d2)
d2.add_transition(69, d2)
d2.add_transition(70, d2)
d2.add_transition(71, d2)
d2.add_transition(72, d2)
d2.add_transition(73, d2)
d2.add_transition(74, d2)
d2.add_transition(75, d2)
d2.add_transition(76, d2)
d2.add_transition(77, d2)
d2.add_transition(78, d2)
d2.add_transition(79, d2)
d2.add_transition(80, d2)
d2.add_transition(81, d2)
d2.add_transition(82, d2)
d2.add_transition(83, d2)
d2.add_transition(84, d2)
d2.add_transition(85, d2)
d2.add_transition(86, d2)
d2.add_transition(87, d2)
d2.add_transition(88, d2)
d2.add_transition(89, d2)
d2.add_transition(90, d2)
d2.add_transition(91, d2)
d2.add_transition(92, d2)
d2.add_transition(93, d2)
d2.add_transition(94, d2)
d2.add_transition(95, d2)
d2.add_transition(96, d2)
d2.add_transition(97, d2)
d2.add_transition(98, d2)
d2.add_transition(99, d2)
d2.add_transition(100, d2)
d2.add_transition(101, d2)
d2.add_transition(102, d2)
d2.add_transition(103, d2)
d2.add_transition(104, d2)
d2.add_transition(105, d2)
d2.add_transition(106, d2)
d2.add_transition(107, d2)
d2.add_transition(108, d2)
d2.add_transition(109, d2)
d2.add_transition(110, d2)
d2.add_transition(111, d2)
d2.add_transition(112, d2)
d2.add_transition(113, d2)
d2.add_transition(114, d2)
d2.add_transition(115, d2)
d2.add_transition(116, d2)
d2.add_transition(117, d2)
d2.add_transition(118, d2)
d2.add_transition(119, d2)
d2.add_transition(120, d2)
d2.add_transition(121, d2)
d2.add_transition(122, d2)
d2.add_transition(123, d2)
d2.add_transition(124, d2)
d2.add_transition(125, d2)
d2.add_transition(126, d2)
d2.add_transition(192, d2)
d2.add_transition(193, d2)
d2.add_transition(194, d2)
d2.add_transition(195, d2)
d2.add_transition(196, d2)
d2.add_transition(197, d2)
d2.add_transition(198, d2)
d2.add_transition(199, d2)
d2.add_transition(200, d2)
d2.add_transition(201, d2)
d2.add_transition(202, d2)
d2.add_transition(203, d2)
d2.add_transition(204, d2)
d2.add_transition(205, d2)
d2.add_transition(206, d2)
d2.add_transition(207, d2)
d2.add_transition(208, d2)
d2.add_transition(209, d2)
d2.add_transition(210, d2)
d2.add_transition(211, d2)
d2.add_transition(212, d2)
d2.add_transition(213, d2)
d2.add_transition(214, d2)
d2.add_transition(215, d2)
d2.add_transition(216, d2)
d2.add_transition(217, d2)
d2.add_transition(218, d2)
d2.add_transition(219, d2)
d2.add_transition(220, d2)
d2.add_transition(221, d2)
d2.add_transition(222, d2)
d2.add_transition(223, d2)
d2.add_transition(224, d2)
d2.add_transition(225, d2)
d2.add_transition(226, d2)
d2.add_transition(227, d2)
d2.add_transition(228, d2)
d2.add_transition(229, d2)
d2.add_transition(230, d2)
d2.add_transition(231, d2)
d2.add_transition(232, d2)
d2.add_transition(233, d2)
d2.add_transition(234, d2)
d2.add_transition(235, d2)
d2.add_transition(236, d2)
d2.add_transition(237, d2)
d2.add_transition(238, d2)
d2.add_transition(239, d2)
d2.add_transition(240, d2)
d2.add_transition(241, d2)
d2.add_transition(242, d2)
d2.add_transition(243, d2)
d2.add_transition(244, d2)
d2.add_transition(245, d2)
d2.add_transition(246, d2)
d2.add_transition(247, d2)
d2.add_transition(248, d2)
d2.add_transition(249, d2)
d2.add_transition(250, d2)
d2.add_transition(251, d2)
d2.add_transition(252, d2)
d2.add_transition(253, d2)
d2.add_transition(254, d2)

d3.isFinalState = True
d3.addToken( 'SYMBOL')
d3.add_transition(9, d2)
d3.add_transition(10, d2)
d3.add_transition(13, d2)
d3.add_transition(33, d2)
d3.add_transition(34, d3)
d3.add_transition(35, d2)
d3.add_transition(36, d2)
d3.add_transition(37, d2)
d3.add_transition(38, d2)
d3.add_transition(39, d2)
d3.add_transition(40, d2)
d3.add_transition(41, d2)
d3.add_transition(42, d2)
d3.add_transition(43, d2)
d3.add_transition(44, d2)
d3.add_transition(45, d2)
d3.add_transition(46, d2)
d3.add_transition(47, d2)
d3.add_transition(48, d2)
d3.add_transition(49, d2)
d3.add_transition(50, d2)
d3.add_transition(51, d2)
d3.add_transition(52, d2)
d3.add_transition(53, d2)
d3.add_transition(54, d2)
d3.add_transition(55, d2)
d3.add_transition(56, d2)
d3.add_transition(57, d2)
d3.add_transition(58, d2)
d3.add_transition(59, d2)
d3.add_transition(60, d2)
d3.add_transition(61, d2)
d3.add_transition(62, d2)
d3.add_transition(63, d2)
d3.add_transition(64, d2)
d3.add_transition(65, d2)
d3.add_transition(66, d2)
d3.add_transition(67, d2)
d3.add_transition(68, d2)
d3.add_transition(69, d2)
d3.add_transition(70, d2)
d3.add_transition(71, d2)
d3.add_transition(72, d2)
d3.add_transition(73, d2)
d3.add_transition(74, d2)
d3.add_transition(75, d2)
d3.add_transition(76, d2)
d3.add_transition(77, d2)
d3.add_transition(78, d2)
d3.add_transition(79, d2)
d3.add_transition(80, d2)
d3.add_transition(81, d2)
d3.add_transition(82, d2)
d3.add_transition(83, d2)
d3.add_transition(84, d2)
d3.add_transition(85, d2)
d3.add_transition(86, d2)
d3.add_transition(87, d2)
d3.add_transition(88, d2)
d3.add_transition(89, d2)
d3.add_transition(90, d2)
d3.add_transition(91, d2)
d3.add_transition(92, d2)
d3.add_transition(93, d2)
d3.add_transition(94, d2)
d3.add_transition(95, d2)
d3.add_transition(96, d2)
d3.add_transition(97, d2)
d3.add_transition(98, d2)
d3.add_transition(99, d2)
d3.add_transition(100, d2)
d3.add_transition(101, d2)
d3.add_transition(102, d2)
d3.add_transition(103, d2)
d3.add_transition(104, d2)
d3.add_transition(105, d2)
d3.add_transition(106, d2)
d3.add_transition(107, d2)
d3.add_transition(108, d2)
d3.add_transition(109, d2)
d3.add_transition(110, d2)
d3.add_transition(111, d2)
d3.add_transition(112, d2)
d3.add_transition(113, d2)
d3.add_transition(114, d2)
d3.add_transition(115, d2)
d3.add_transition(116, d2)
d3.add_transition(117, d2)
d3.add_transition(118, d2)
d3.add_transition(119, d2)
d3.add_transition(120, d2)
d3.add_transition(121, d2)
d3.add_transition(122, d2)
d3.add_transition(123, d2)
d3.add_transition(124, d2)
d3.add_transition(125, d2)
d3.add_transition(126, d2)
d3.add_transition(192, d2)
d3.add_transition(193, d2)
d3.add_transition(194, d2)
d3.add_transition(195, d2)
d3.add_transition(196, d2)
d3.add_transition(197, d2)
d3.add_transition(198, d2)
d3.add_transition(199, d2)
d3.add_transition(200, d2)
d3.add_transition(201, d2)
d3.add_transition(202, d2)
d3.add_transition(203, d2)
d3.add_transition(204, d2)
d3.add_transition(205, d2)
d3.add_transition(206, d2)
d3.add_transition(207, d2)
d3.add_transition(208, d2)
d3.add_transition(209, d2)
d3.add_transition(210, d2)
d3.add_transition(211, d2)
d3.add_transition(212, d2)
d3.add_transition(213, d2)
d3.add_transition(214, d2)
d3.add_transition(215, d2)
d3.add_transition(216, d2)
d3.add_transition(217, d2)
d3.add_transition(218, d2)
d3.add_transition(219, d2)
d3.add_transition(220, d2)
d3.add_transition(221, d2)
d3.add_transition(222, d2)
d3.add_transition(223, d2)
d3.add_transition(224, d2)
d3.add_transition(225, d2)
d3.add_transition(226, d2)
d3.add_transition(227, d2)
d3.add_transition(228, d2)
d3.add_transition(229, d2)
d3.add_transition(230, d2)
d3.add_transition(231, d2)
d3.add_transition(232, d2)
d3.add_transition(233, d2)
d3.add_transition(234, d2)
d3.add_transition(235, d2)
d3.add_transition(236, d2)
d3.add_transition(237, d2)
d3.add_transition(238, d2)
d3.add_transition(239, d2)
d3.add_transition(240, d2)
d3.add_transition(241, d2)
d3.add_transition(242, d2)
d3.add_transition(243, d2)
d3.add_transition(244, d2)
d3.add_transition(245, d2)
d3.add_transition(246, d2)
d3.add_transition(247, d2)
d3.add_transition(248, d2)
d3.add_transition(249, d2)
d3.add_transition(250, d2)
d3.add_transition(251, d2)
d3.add_transition(252, d2)
d3.add_transition(253, d2)
d3.add_transition(254, d2)

