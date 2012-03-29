# Marcus M. Darden -- 2012-02-20
# rand.asm: A pseudorandom number generator function
# Registers: A callee-saved function using only $s registers
#	$s0-s3 -	For temporary calculations
# I revisited this file in CS140 2012-03-29
# I Re-Revisited this file...

	.text
get_random:				# Function entry for get_random()
	subu	$sp, $sp, 32		# Establish stack frame
	sw	$s0, 0($sp)		# store s0
	sw	$s1, 4($sp)		# store s1
	sw	$s2, 8($sp)		# store s2
	sw	$s3, 12($sp)		# store s3
	sw	$fp, 16($sp)		# store frame pointer
	addu	$fp, $sp, 32		# establish new frame pointer
	lw	$s1, m_w		# load m_w seed
	lw	$s2, m_z		# load m_z seed

	## m_z = 36969 * (m_z & 65535) + (m_z >> 16)
	and	$s0, $s2, 0xFFFF	# s0 = m_z & 1111 1111
	li	$s3, 36969		# s3 = 36969
	multu	$s3, $s0		# s3 * s0
	mflo	$s0			# s0 = low half
	srl	$s3, $s2, 0x10		# s3 = m_z >> 16
	addu	$s2, $s0, $s3		# m_z = ...
	sw	$s2, m_z

	## m_w = 18000 * (m_w & 65535) + (m_w >> 16)
	and	$s0, $s1, 0xFFFF	# s0 = m_w & 1111 1111
	li	$s3, 18000		# s3 = 18000
	multu	$s3, $s0		# s3 * s0
	mflo	$s0			# s0 = low half
	srl	$s3, $s1, 0x10		# s3 = m_w >> 16
	addu	$s1, $s0, $s3		# m_w = ...
	sw	$s1, m_w

	## (m_z << 16) + m_w
	sll	$v0, $s2, 0x10		# v0 = m_z << 16
	addu	$v0, $v0, $s1		# v0 = v0 + m_w	

	lw	$fp, 16($sp)		# restore frame pointer
	lw	$s3, 12($sp)		# restore s3
	lw	$s2, 8($sp)		# restore s2
	lw	$s1, 4($sp)		# restore s1
	lw	$s0, 0($sp)		# restore s0
	addu	$sp, $sp, 32		# restore stack pointer
	jr	$ra			# Return from the function

	.data
m_w:		.word 65536
m_z:		.word 1668
