import os

def recursive_hide_in_folder(path):
  h = []
  for f in os.listdir(path):
    full = os.path.join(path,f)
    if f.endswith(".import"):
      h.append(f)
    elif os.path.isdir(full):
      recursive_hide_in_folder(full)
  if len(h) > 0:
    with open(os.path.join(path,".hidden"),"w+") as hf:
      hf.write("\n".join(h))

recursive_hide_in_folder(".")
