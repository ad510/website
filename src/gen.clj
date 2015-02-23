(ns gen (:require [net.cgrand.enlive-html :as html]
                  [me.raynes.fs :as fs]))

(html/deftemplate base "base.htm" [url title]
  [:title] (html/content title)
  [[:a (html/attr= :href url)]] (html/add-class "sel")
  [:#pgcontent] (html/html-content (slurp (str "src/pg/" url))))

(defn -main []
  (fs/delete-dir "src/out")
  (fs/copy-dir "src/static" "src/out")
  (doseq [f (.list (fs/file "src/pg"))]
    (spit (str "src/out/" f) (apply str (base f "my title")))))
