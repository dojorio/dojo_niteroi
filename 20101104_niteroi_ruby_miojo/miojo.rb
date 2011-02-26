def miojo(h_small, h_big, miojo) 
   
  h1 = h_small
  h2 = h_big
  total = 0
  
  while h1 != miojo && h2 != miojo
    if (h2 > h1)
      h2 -= h1
      total += h1
      h1= h_small
    else
      total += h2
      h1 -= h2
      h2 = h_big 
    end
  end
  return total+miojo
  
end
