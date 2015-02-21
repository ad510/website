(ns gen (:require [net.cgrand.enlive-html :as html]
                  [me.raynes.fs :as fs]))

(html/deftemplate base "base.htm" [title body]
  [:head :title] (html/content title)
  [:body] (html/content body))

(defn -main []
  (fs/delete-dir "src/out")
  (fs/mkdir "src/out")
  (doseq [f (.list (fs/file "src/pg"))]
    (spit (str "src/out/" f) (apply str (base "my title" (slurp (str "src/pg/" f)))))))
