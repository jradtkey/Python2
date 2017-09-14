SELECT * 
FROM users
LEFT JOIN friendships on friendships.id = users.id
LEFT JOIN users as user2 ON users.id = friendships.id
